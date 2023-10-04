from selenium import webdriver
from login_and_perform import Login
import pandas

AccountsToFollow_Df = pandas.read_csv(
    r"Day 52\Insta-Folllower-Bot\Data\accounts_list.csv"
)
AccountsToFollow = AccountsToFollow_Df.account.tolist()

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)

loginn = Login(driver)
loginn.logintoinsta()
for account in AccountsToFollow:
    loginn.followerBot(account)

driver.quit()
