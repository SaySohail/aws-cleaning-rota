import os
import json
from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd
import requests
import yaml


# -------- Config loading --------
def load_config(path: str = "config.yaml") -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    # Minimal validation
    whatsapp = cfg.get("whatsapp", {})
    if not whatsapp.get("api_url"):
        raise ValueError("Missing required config: whatsapp.api_url")
    # Allow ACCESS_TOKEN override via env var for safer secret handling
    whatsapp["access_token"] = os.getenv("WHATSAPP_ACCESS_TOKEN", whatsapp.get("access_token"))
    if not whatsapp.get("access_token"):
        raise ValueError(
            "Missing WhatsApp access token. Provide in config.yaml under whatsapp.access_token "
            "or set environment variable WHATSAPP_ACCESS_TOKEN."
        )
    cfg["whatsapp"] = whatsapp

    schedule = cfg.get("schedule", {})
    if not schedule.get("workbook"):
        raise ValueError("Missing required config: schedule.workbook")
    if not schedule.get("timezone"):
        schedule["timezone"] = "UTC"
    cfg["schedule"] = schedule

    cfg.setdefault("contacts", {})
    return cfg


CONFIG = load_config()  # loaded once per container


# -------- Helpers --------
def get_mobile_number(name: str) -> str:
    return CONFIG["contacts"].get(name, "+44XXXXXXXXXX")


def send_whatsapp_message(phone_number: str, message: str, whatsapp_api_url: str, access_token: str) -> requests.Response:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "preview_url": False,
        "to": phone_number,
        "type": "text",
        "text": {"body": message},
    }
    return requests.post(whatsapp_api_url, headers=headers, json=data, timeout=15)


def load_rota_dataframe(workbook: str, sheet_name: str | None = None) -> pd.DataFrame:
    df = pd.read_excel(workbook, sheet_name=sheet_name)
    # Normalize date column
    if "Dates" not in df.columns:
        raise KeyError("Expected a 'Dates' column in the rota file.")
    df["Dates"] = pd.to_datetime(df["Dates"], errors="coerce")
    return df


# -------- Lambda handler --------
def lambda_handler(event, context):
    tz = ZoneInfo(CONFIG["schedule"]["timezone"])
    today = datetime.now(tz).date()

    workbook = CONFIG["schedule"]["workbook"]
    sheet_name = CONFIG["schedule"].get("sheet_name")

    whatsapp_api_url = CONFIG["whatsapp"]["api_url"]
    access_token = CONFIG["whatsapp"]["access_token"]

    rota_data = load_rota_dataframe(workbook, sheet_name)
    # filter rows where Dates == today (date-only)
    todays_tasks = rota_data[rota_data["Dates"].dt.date == today]

    if todays_tasks.empty:
        print(f"No tasks found for today: {today.isoformat()}")
        return {"status": "ok", "messages_sent": 0}

    # assume first matching row; tasks start from column 2 onward
    row = todays_tasks.iloc[0]
    sent = 0
    failures = []

    for task_col in rota_data.columns[1:]:
        person = str(row.get(task_col, "")).strip()
        if not person:
            continue

        phone_number = get_mobile_number(person)
        message = f"Reminder for {person}: Please complete your cleaning task - {task_col} on {today.strftime('%Y-%m-%d')}"

        try:
            resp = send_whatsapp_message(phone_number, message, whatsapp_api_url, access_token)
        except requests.RequestException as e:
            print(f"[ERROR] Network issue sending to {person}: {e}")
            failures.append({"person": person, "error": str(e)})
            continue

        if resp.status_code == 200:
            try:
                payload = resp.json()
            except ValueError:
                payload = {"note": "non-JSON success response"}
            print(f"[OK] Sent to {person}: {json.dumps(payload)[:500]}")
            sent += 1
        else:
            body_preview = resp.text[:500]
            print(f"[FAIL] {person}: HTTP {resp.status_code} - {body_preview}")
            failures.append({"person": person, "status": resp.status_code, "body": body_preview})

    return {"status": "ok", "messages_sent": sent, "failures": failures}


# ---- Local test (comment out on AWS) ----
if __name__ == "__main__":
    print(lambda_handler(None, None))
