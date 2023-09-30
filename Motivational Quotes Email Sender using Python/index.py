import smtplib
import requests

EMAIL_HOST_USER = "your email id"
EMAIL_HOST_PASSWORD = "your app password (generate it from gmail app passwords)"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)

def get_random_quote():
    url = f'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&category=inspire'
    response = requests.get(url)
    data = response.json()
    return data["quoteText"]


connection.sendmail(from_addr=EMAIL_HOST_USER,to_addrs="recpeient address",msg=f"Subject:Today's Motivation \n\n {get_random_quote()}")


connection.close()
