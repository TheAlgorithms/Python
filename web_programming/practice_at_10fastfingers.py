from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys
import time

if __name__== "__main__":
    print("Give the letter you want to practice")

    """
    only one character to practice
    """
    a = sys.stdin.read(1)

    """
    10fastfingers url
    """
    url1 = "https://10fastfingers.com/widgets/typingtest"

    """
    a website that contains words of each letter
    """
    url2 = "https://www.thefreedictionary.com/words-containing-"+a

    """
    urlopen to the website with the words in order to use in BeautifulSoup
    """
    try:
        p1 = urlopen(url2)
    except:
        print("Error opening the URL")

    """
    getting the html content using BeautifulSoup
    """
    soup = BeautifulSoup(p1, "html.parser")

    """
    right now the program will only find words with 5 or 6 letters
    """
    l1=soup.find_all("div", {"id": "w6"})
    l2=soup.find_all("div", {"id": "w5"})

    """
    fitlering the html in order to get the words
    """
    for tag in l1:
        w6=tag.find_all("a")

    for tag in l2:
        w5=tag.find_all("a")

    """
    building the words to format that can be used by 10fastfingers url
    """
    str=""
    for x in w6:
        str=str+x.text+"|"
    for x in w5:
        str=str+x.text+"|"

    try:

        """
        webdriver from selenium that will open 10fastfingers website in chrome
        """
        driver = webdriver.Chrome("webdrivers\chromedriver.exe")
        driver.get(url1)
        driver.implicitly_wait(50)

        """
        finding the cookies pop-up and pressing ok or else the program will crush
        """
        inputB1 = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonAccept")
        print(inputB1.text)
        time.sleep(1)
        inputB1.click()
        time.sleep(1)

        """
        opening settings-link in order to insert the edited string
        """
        inputB2 = driver.find_element_by_id("settings-link")
        driver.implicitly_wait(50)
        time.sleep(1)
        inputB2.click()
        driver.implicitly_wait(50)

        """
        inserting the edited string to type-words-to-practice area
        """
        inputElement = driver.find_element_by_tag_name("textarea")
        inputElement.clear()
        inputElement.send_keys(str)

    except NoSuchElementException as e:
        print(e)
