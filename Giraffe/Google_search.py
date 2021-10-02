from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = "https://www.google.com"
driver.get(url)
driver.minimize_window()
print("Loading")
item = input("Enter what to search for on google: ")
search = driver.find_element_by_xpath("""//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input""")
search.send_keys(item)
search.submit()