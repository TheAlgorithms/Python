import smtplib, ssl
from email.mime.multipart  import MIMEMultipart
from email.mime.text  import MIMEText
from datetime import datetime
import time


def send_email(smtp_server, port, sender_email, password, receiver_email, subject, body):
    msg=MIMEMultipart()
    msg['From']=sender_email
    msg['To']=receiver_email
    msg['Subject']=subject
    msg.attach(MIMEText(body,'html'))

    server=smtplib.SMTP(smtp_server,port)
    server.starttls()
    server.login(sender_email,password)
    server.send_message(msg)
    server.quit()

server = 'smtp.gmail.com'
port=587


# Either write the email and password in the python script or use environment variables(MORE SECURE)
sender_email = "sender_email@gmail.com"     # Write your email through which you want to send the mail 
password= "XXXX"                            # Generate and write your App password for the above email after enabling 2-factor authentication
receiver_email = "recipient@test.com"       # Write the email of the receiving party


subject="Test Mail sent using python bot"   # Add the subject for your email
body="<p> Hey there, this message has been sent using a <b> python bot </b>. This is the content of the email you want to send. Make the <i> required modifications </i> to this message. </p>"                      # Add the content of you email


scheduled_time_str = "23:24:00"             # Enter the scheduled time when you want to send the email in format HH:MM:SS
current_time_str = time.strftime("%H:%M:%S")

scheduled_time = datetime.strptime(scheduled_time_str, "%H:%M:%S")
current_time = datetime.strptime(current_time_str, "%H:%M:%S")

time_difference = scheduled_time - current_time
total_seconds = time_difference.total_seconds()


while True:
    if current_time == scheduled_time:
        send_email(server,port,sender_email, password,receiver_email,subject,  body)
        time.sleep(20)
        print("Email has been sent")
        break
    else:
        print(total_seconds)
        time.sleep(total_seconds)
        send_email(server,port,sender_email, password,receiver_email,subject,  body)
        print("Email has been sent")
        break
