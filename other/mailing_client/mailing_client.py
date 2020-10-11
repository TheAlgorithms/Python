import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587) #enter your smtp server here. I've used google's one.
server.ehlo()
server.starttls()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('sender@email.com', password) #sender's email here at example@gmail.com and edit the password file with the sender's email's password.
msg = MIMEMultipart()
msg['from'] = 'laptop'
msg['to'] = '' #enter designated email here/ reciver@email.com
msg['subject'] = 'just a test'

with open('msg.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))    

filename  = 'wolf.jpg' #attach additional files here. I've attached a jpeg
attachment = open(filename, 'rb') #reading byte mode for images

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('sender@email.com', 'reciever@email.com', text )