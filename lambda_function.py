import openpyxl
import requests
from datetime import datetime
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

mobile_numbers = {
    'Sohail': '+447442997272',
    'Vishnu': '+447767991451',
    'Sujata': '+447778456215',
    'Sumit': '+447585865960',
    'Bineesha': '+447466624343',
    'Vandana': '+447867215257',
    # Add more names and numbers as needed
}

def get_mobile_number(name):
    return mobile_numbers.get(name, '+919535409325')


account_sid = 'ACa2676bf9648e416272ddaef654c9bbce'
auth_token = 'c0ca4e4d49e6b9c00b5b47a92acd97ef'
twilio_client = Client(account_sid, auth_token)
from_number='+447897034712'

def send_whatsapp_message_twilio(phone_number,message_body):
    try:

        message = twilio_client.messages.create(
            body=message_body,
            from_=from_number,
            to=f'whatsapp:{phone_number}'
        )
        return message.sid
    except TwilioRestException as e:
        print(f'Failed to send message: {e}')
        return None

def send_text_message_twilio(phone_number,message_body):
    try:

        message = twilio_client.messages.create(
            body=message_body,
            from_=from_number,
            # media_url=['https://img.randme.me/'],
            to=phone_number
        )
        return message.sid
    except TwilioRestException as e:
        print(f'Failed to send message: {e}')
        return None

# Function to send WhatsApp message
def send_whatsapp_message(phone_number, message, whatsapp_api_url, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type': 'individual',
        'preview_url': False,
        'to': phone_number,
        'type': 'text',
        'text': {'body': message}
    }
    response = requests.post(whatsapp_api_url, headers=headers, json=data)
    return response




# Lambda handler function
def lambda_handler(event, context):
    # Load the Excel data using openpyxl
    try:
        workbook = openpyxl.load_workbook('Rota-Berkshire.xlsx')
        sheet = workbook.active
    except Exception as e:
        print(f"Error Loading Excel file: {e}")
        return

    # Get today's date
    today = datetime.now().date()
    whatsapp_api_url = 'https://graph.facebook.com/v18.0/125836087288807/messages'
    access_token = 'EAAhBEy9TVtgBO0beIIbd8J48bf0n59lZCRAGnU0Ym8Tgj4qPb4H6HGujZClN2c2txG7cdbqGi0h4DWYfpZAYfYG2NUBQWx2NOE9sJLXvBM8nsTlvn6d1s8tT5WXUwvR4ZCI0aaj5G16dQmHOZA2PGZCNktxd2MqmvCZAI4ShdjhwLTeNaC1NZBFFqFzCXQcw'
    # Initialize a variable to check if tasks are found for today
    tasks_found = False

    # Iterate through the rows and find today's tasks
    for row in sheet.iter_rows(min_row=2):  # Assuming the first row is the header
        task_date = row[0].value
        if task_date and task_date.date() == today:
            tasks_found = True
            for col_index, cell in enumerate(row[1:], start=2):  # Skip the date cell
                person = cell.value
                if person:  # Check if the cell is not empty
                    task = sheet.cell(row=1, column=col_index).value  # Get the task name from the header
                    phone_number = get_mobile_number(person)
                    message = f"Reminder for {person}: Please complete your cleaning task - {task} on {today.strftime('%Y-%m-%d')} \n \n"
                    # response = send_whatsapp_message(phone_number, message, whatsapp_api_url, access_token)
                    message_sid = send_text_message_twilio(phone_number, message)
                    if message_sid:
                        print(f"Message sent successfully to {person}: {message_sid}")
                    else:
                        print(f"Failed to send message to {person}")
   

                    # # Handle the response
                    # if response.status_code == 200:
                    #     print(f"Message sent successfully to {person}")
                    # else:
                    #     print(f"Failed to send message to {person}")

    if not tasks_found:
        print("No tasks found for today")


# Testing the function locally (comment out when deploying)
lambda_handler(None, None)
