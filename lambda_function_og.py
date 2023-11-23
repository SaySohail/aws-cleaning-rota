import pandas as pd
import requests
from datetime import datetime

mobile_numbers = {
    'Sohail': '+919535409325',
    'Vishnu': '+919535409325',
    'Sujata': '+917587041710',
    'Sumit': '+919535409325',
    'Bineesha': '+919535409325',
    'Vandana': '+919535409325',
    # Add more names and numbers as needed
}

def get_mobile_number(name):
    return mobile_numbers.get(name, '+919535409325')


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
    # Load the Excel data
    rota_data = pd.read_excel('Rota-Berkshire.xlsx')

    # Get today's date
    today = datetime.now().date()

    # Find today's tasks
    todays_tasks = rota_data[rota_data['Dates'].dt.date == today]

    # WhatsApp API URL and Token (these should be environment variables)
    whatsapp_api_url = 'https://graph.facebook.com/v18.0/125836087288807/messages'
    access_token = 'EAAhBEy9TVtgBO0beIIbd8J48bf0n59lZCRAGnU0Ym8Tgj4qPb4H6HGujZClN2c2txG7cdbqGi0h4DWYfpZAYfYG2NUBQWx2NOE9sJLXvBM8nsTlvn6d1s8tT5WXUwvR4ZCI0aaj5G16dQmHOZA2PGZCNktxd2MqmvCZAI4ShdjhwLTeNaC1NZBFFqFzCXQcw'

    if not todays_tasks.empty:
        for task in todays_tasks.columns[1:]:
            person = todays_tasks[task].values[0]
            phone_number = get_mobile_number(person) 
            message = f"Reminder for {person}: Please complete your cleaning task - {task} on {today.strftime('%Y-%m-%d')}"
            response = send_whatsapp_message(phone_number, message, whatsapp_api_url, access_token)
            # Handle the response
            if response.status_code == 200:
                try: 
                    response_json = response.json()
                    print("Response JSON:", response_json)
                except ValueError:
                    print("Error In JSON")
                print(f"Message sent successfully to {person}")
            else:
                print(f"Failed to send message to {person}")
    else:
        print("No tasks found for today")

# Testing the function locally (comment out when deploying)
lambda_handler(None, None)
