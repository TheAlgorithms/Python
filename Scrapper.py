import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import shutil
import urllib
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

def job(searchString):
    searchUrl = "https://www.google.com/search?q="+searchString+"&source=lnms&tbm=isch"
    result = requests.get(searchUrl)

# if successful parse the download into a BeautifulSoup object, which allows easy manipulation
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")

    div = soup.findAll('img',{'class':'yWs4tf'})

    f= open("urls.txt","w+")
    for i in div:
        f.write(i['src']+'\n')
    f.close()

    with open('urls.txt') as f:
        lines = [line.rstrip() for line in f]


    os.mkdir('kaks')
    for i,j in enumerate(lines):
        jojo= urllib.request.urlretrieve(j,'img'+str(i)+'.jpg')
        os.rename(jojo[0], "kaks/"+jojo[0])

    shutil.make_archive('kaks', 'zip', 'kaks')


def email(usermail,password,clientemail):

    msg = MIMEMultipart()
    filename='kaks.zip'
    attachment  =open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
    text = msg.as_string()
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)

    server.login(usermail,password)
    server.sendmail(usermail,clientemail,text)
    server.quit()

def main_job(year,month,date,hour,minute,second,name,username,password,clientmail):
    sendtime = datetime.datetime(year,month,date,hour,minute,second)
    st = sendtime.timestamp()
    t = time.time()
    print(f"scheduled time:{year}-{month}-{date}-{hour}-{minute}-{second}")

    x = time.sleep(st - t)
    job(name)
    time.sleep(15)
    email(username,password,clientmail)
    print("done")


#main_job(year,month,date,hour,minute,second,name of the thing,your email id,your password,client's email id)

main_job(2021,8,12,17,00,00,"cats","youremailid","password","clientemailid")



"""if there is a gmail authentication erron..........


https: // myaccount.google.com / lesssecureapps?pli = 1 & rapt = AEjHL4NoPGAIuu_It757bkDeFtPrGVtbKB9FnMFUVkkp4Nhhldhmqm4jR0jTujaRMutCqVPZwNRbpbgsddZCDTVmGjxp4Pe2jg

........go here and allow less secure apps"""

