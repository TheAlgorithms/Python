import pandas as pd
import datetime
import smtplib
#Enter your email id and password
GMAIL_ID=''
GMAIL_PSWD=''


def sendEmail(to,sub,msg):
    #print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID,to,f"Subject: {sub}\n\n{msg}")
    s.quit()
if __name__=="__main__":
    #sendEmail(TO,"Subject","Test mail")
    #exit()
    df=pd.read_excel("data.xlsx")
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%Y")
    #print(type(today))
    #print(today)
    writeInd=[]
    for index,item in df.iterrows():
        #print(index,item["Birthday"])
        bday=item["Birthday"].strftime("%d-%m")
        if(bday==today) and yearNow not in str(item["Year"]):
            writeInd.append(index)
            sendEmail(item["Email"],"Happy Birthday",item["Dialogue"])
    if(len(writeInd)>0):
        
        for i in writeInd:
            yr=df.loc[i,"Year"]
            df.loc[i,'Year']=str(yr)+','+str(yearNow)
        
    df.to_excel('data.xlsx',index=False)
