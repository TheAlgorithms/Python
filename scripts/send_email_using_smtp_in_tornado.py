import asyncio
import tornado.ioloop, tornado.web
import smtplib

# Function for sending mail
def sendEmail(recipient_email, app_name): 
    sender_email = ""
    app_password = ""
    # SMTP config
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    subject = "Android App Created: %s" % app_name
    body = '''Your Android app %s has been successfully created.''' % app_name
    
    email_message = "Subject: %s\n\n%s" % (subject, body)
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, email_message)
        print("Email sent successfully")
        email_sent = True
        
    except smtplib.SMTPAuthenticationError as e:
        print("SMTP Authentication Error: %s" % e)
    except Exception as e:
        print("Error: %s", e)

    # raise exception for outer try except
    if not email_sent:
        raise Exception("Email sending failed.")



# Async testing function
async def asyncFunc(i):
    await asyncio.sleep(1)
    print("I'm Running %s" % i)


# main function
async def main():
    print("Code started")

    # Code for sending mail
    try:         
        recipient_email = "anupesh.verma@edugorilla.org"
        app_name = "myApp"
        tornado.ioloop.IOLoop.current().run_in_executor(None, sendEmail, recipient_email, app_name)
      # You can directly call the function for async
      # sendEmail(recipient_email, app_name)
    except Exception as e:
        print(e)

    for i in range(0, 10):
        await asyncFunc(i)
        

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
