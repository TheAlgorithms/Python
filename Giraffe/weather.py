from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time
import io
from PIL import Image

def NotFoundError():
    print("You have entered incorrect city....Try again..")

def Error(str):
    print("Error " +str+" value not found.. ")

def BuildGraph():
    ss=driver.find_element_by_xpath("""//*[@id="chart_small"]""").screenshot_as_png
    imageStream = io.BytesIO(ss)
    im = Image.open(imageStream)
    im.show()

#for selenium initz
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# current directory
PATH ="C:\Program Files (x86)\chromedriver.exe"
driver =webdriver.Chrome(options=chrome_options, executable_path=PATH)

URL="https://openweathermap.org/find"
driver.get(URL)
driver.minimize_window()
city=input("Please correctly enter your city...")
inputCity=driver.find_element_by_xpath("""//*[@id="search_str"]""")
inputCity.send_keys(city)
inputCity.submit()
time.sleep(3)
try:
  alert=driver.find_element_by_xpath("""//*[@id="forecast_list_ul"]/div""")
  NotFoundError()
except:
    cityname = driver.find_element_by_xpath("""//*[@id="forecast_list_ul"]/table/tbody/tr/td[2]/b[1]""")
    cityname.click()
    time.sleep(3)
    localtime = driver.find_element_by_xpath("""//*[@id="weather-widget-local-time"]""").text
    print("Local Time : " + localtime)
    wind = driver.find_element_by_xpath("""//*[@id="weather-widget-wind"]""").text
    print("Wind :" + wind)
    cloud = driver.find_element_by_xpath("""//*[@id="weather-widget-cloudiness"]""").text
    print("Cloudiness :" + cloud)
    pressure = driver.find_element_by_xpath("""//*[@id="weather-widget-pressure"]""").text
    print("Pressure :" + pressure)
    try:
       humidity = driver.find_element_by_xpath("""//*[@id="weather-widget-humidity"]""").text
       print("Humidity :" + humidity)
    except:
       Error("Humidity")
    try:
      rain=driver.find_element_by_xpath("""//*[@id="weather-widget-rain"]""").text
      print("Rain :"+rain)
    except:
      Error("Rain")
ans=input("Do you want to build graph for temp....\n")
if ans=="Yes" or ans=="yes" or ans=="YES" or ans=="y" or ans=="Y":
    BuildGraph()

