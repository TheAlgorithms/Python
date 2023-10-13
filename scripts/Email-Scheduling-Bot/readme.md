# Python Email Scheduler

This Python script allows you to send scheduled emails using Gmail's SMTP server. You can specify the recipient's email address, subject, and the content of the email to be sent at a particular scheduled time.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- Access to a Gmail account from which you want to send emails.
- App password generated for your Gmail account (You must enable 2-factor authentication and then generate the App password for your email.)

## Installation

1. Clone or download this repository to your local machine.
2. Open the Python script (`email_scheduler.py`) in a code editor or IDE.

## Configuration

Before running the script, you need to configure it with your Gmail account details and the email details you want to send.

1. Replace the following placeholders in the script with your own information:
   - `sender_email`: Your Gmail email address.
   - `password`: Your Gmail app password or account password (use environment variables for security).
   - `receiver_email`: The recipient's email address.
   - `subject`: The subject of your email.
   - `body`: The content of your email (you can use HTML tags for formatting).

2. Set the `scheduled_time_str` variable to the time when you want the email to be sent. The format should be HH:MM:SS.

## Usage

To use the script, follow these steps:

1. Configure the script as described in the "Configuration" section.
2. Run the script using your Python interpreter.

The script will check the current time against the scheduled time and send the email when the scheduled time is reached. It will print a message to the console indicating that the email has been sent.

## Security Considerations

- Using environment variables for storing your email and password is more secure than hardcoding them in the script. Implement that if needed.
- App passwords are recommended for Gmail accounts as they provide an additional layer of security.
