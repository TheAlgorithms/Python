#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def send_email():
    """
    Send email to a user
    """
    html = Template(Path("index.html").read_text())
    email = EmailMessage()
    email["from"] = "John Doe"
    email["to"] = "<to email address>"
    email["subject"] = "You won 1,000,000 dollars!"

    email.set_content(html.substitute({"name": "Jenny Doe"}), "html")

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("<your email address>", "<your password>")
        smtp.send_message(email)
