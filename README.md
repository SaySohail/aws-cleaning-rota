# WhatsApp Cleaning Rota Notifier

<div align="center">
  <img src="images/logo.png" alt="Logo" width="80" height="80">
  <h3 align="center">Automated Cleaning Task Reminder System</h3>
</div>

## Description
The WhatsApp Cleaning Rota Notifier is a serverless solution designed to automate the process of sending cleaning task reminders. Leveraging AWS Lambda and the Twilio API, this project efficiently notifies individuals of their scheduled cleaning duties according to a predefined rota, ensuring timely task completion and effective communication.

## Features
- **Automated WhatsApp Notifications**: Sends reminders for cleaning tasks directly to individuals' WhatsApp.
- **Serverless Architecture**: Utilizes AWS Lambda for running the application without the need for server management.
- **Scheduled Triggering**: Employs AWS EventBridge for timely execution of the function on specified days and times.
- **Twilio WhatsApp Integration**: Relies on Twilio API for seamless and reliable messaging.
- **Excel-based Rota Management**: Easy to manage and update the cleaning schedule through an Excel file.
- **Environment Friendly**: Reduces the need for paper-based schedules and manual follow-ups.

## How It Works
1. **Rota Schedule**: An Excel file (`Rota-Berkshire.xlsx`) contains the cleaning schedule, assigning tasks to individuals.
2. **Function Trigger**: AWS EventBridge triggers the Lambda function on pre-set days (Mondays and Thursdays at 9 AM UTC).
3. **Message Dispatch**: Upon execution, the Lambda function reads the schedule and sends WhatsApp messages to the designated individuals.

## Setup and Deployment

### Prerequisites
- AWS account with access to Lambda and EventBridge services.
- Twilio account with a WhatsApp-enabled phone number.
- Python environment for local setup.

### Dependencies
- `openpyxl` for Excel file handling.
- `requests` for making HTTP requests.
- `twilio` for Twilio API integration.

### Deployment Steps
1. **Prepare the Deployment Package**: Package the Python script along with its dependencies.
2. **Deploy to AWS Lambda**: Upload the package to AWS Lambda and configure the function.
3. **Set EventBridge Rules**: Configure rules to trigger the function as per the schedule.

## Configuration
- Set environment variables in AWS Lambda for Twilio credentials and phone numbers.
- Update the `Rota-Berkshire.xlsx` file to reflect the current schedule.

## Usage
Update the cleaning rota in the Excel file as needed, and the system will handle the rest, ensuring individuals receive timely notifications.

## Contributing
Contributions to the project are welcome. Please ensure to follow the best practices and coding standards.

## Contact
- Your Name - [@SayedSohail10](https://twitter.com/SayedSohail10)
- Email - peerzadesayedsohail@gmail.com
- Project Link: [https://github.com/SaySohail/aws-cleaning-rota](https://github.com/SaySohail/aws-cleaning-rota)
