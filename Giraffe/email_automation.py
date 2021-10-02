from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#intialize
PATH ="C:\Program Files (x86)\chromedriver.exe"

#host_email = input("Enter the email from which mails need to be send:\n")
#host_password = input("Enter the Password:\n")
host_email = "ishwinfo@gmail.com"
host_password = "ABC!@#$%"
#message details here
to = "aikansh1goel7@gmail.com"
message = "Hi"
subjects = "asb"


#setting up chrome
url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver = webdriver.Chrome(PATH)
driver.get(url)

email_input = driver.find_element_by_xpath("""//*[@id="identifierId"]""")
email_input.send_keys(host_email)

email_sumbit = driver.find_element_by_xpath("""//*[@id="identifierNext"]/div/button""")
email_sumbit.click()

time.sleep(10)

password_input = driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""")
password_input.send_keys(host_password)

next = driver.find_element_by_xpath("""//*[@id="passwordNext"]/div/button/div[2]""")
next.click()

time.sleep(15)

#add loop from here

compose = driver.find_element_by_xpath("""/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div""")
compose.click()

time.sleep(5)

recipient = driver.find_element_by_name("to")
recipient.send_keys(to)

subject = driver.find_element_by_xpath("""/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div/input""")
subject.send_keys(subjects)

body = driver.find_element_by_xpath("""/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div""")
body.send_keys(message)

submit = driver.find_element_by_xpath("""/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]""")
submit.click()
print("message send")
time.sleep(1)
#loop till here
driver.close()
driver.quit()