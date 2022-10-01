"""
Selenium automation script that checks for unread messages from a specific
whatsapp contact and responds with a random message from a set of responses
"""

import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Name of the Person you want to automate repleies for (as saved in your contacts)
NAME = "John Doe"

# Can use this list of messages to send text randomly
# (optional, since the script currently uses chatterbot)
RESPONSES = ["Hi there", "What's up", "Oh", "ttyl"]

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=<Your_browser_user_profile>")
driver = webdriver.Chrome(service=Service("./chromedriver"), options=options)
# driver.maximize_window()

print("Opening Whatsapp")
driver.get("https://web.whatsapp.com")

input("Press enter when whatsapp has loaded ")


def send_message(text) -> None:
    print(f"Opening chat for {NAME}")
    user = driver.find_element(by=By.XPATH, value=f'//span[@title="{NAME}"]')
    user.click()
    time.sleep(2)
    messages = driver.find_elements(by=By.XPATH, value='//div[@class="_22Msk"]')
    print(messages[-1])
    print("Clicking text box")
    box = driver.find_element(by=By.XPATH, value='//div[@title="Type a message"]')
    box.click()
    # msg = random.choice(MESSAGES)
    msg = str(text)
    print(f"Typing {msg}")
    box.send_keys(msg)
    print("Clicking send")
    time.sleep(2)
    send_btn = driver.find_element(
        by=By.XPATH, value='//button[@data-testid="compose-btn-send"]'
    )
    send_btn.click()
    time.sleep(3)


xp = './/span[@class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae"]'


def has_unread() -> bool:
    all_chats = driver.find_elements(by=By.XPATH, value='//div[@class="_3OvU8"]')
    for chat in all_chats:
        try:
            our_target = chat.find_element(
                by=By.XPATH, value=f'.//span[@title="{NAME}"]'
            )
            title = our_target.get_attribute("title")
            if title == NAME:
                print("Found " + title)
                try:
                    chat.find_element(by=By.XPATH, value='.//div[@class="_1pJ9J"]')
                    print("Found Unread message(s) from " + NAME)
                    return True
                except Exception:
                    print("No Unread messages from " + NAME)
                break
        except Exception:
            our_target = chat.find_element(
                by=By.XPATH,
                value=xp,
            )
            # print(our_target.get_attribute("title"))
            continue
    return False


def get_last_message() -> str:
    print(f"Opening chat for {NAME}")
    user = driver.find_element(by=By.XPATH, value=f'//span[@title="{NAME}"]')
    user.click()
    time.sleep(2)
    messages = driver.find_elements(by=By.XPATH, value='//div[@class="_22Msk"]')
    last_msg = (
        messages[-1]
        .find_element(
            by=By.XPATH, value='.//span[@class="i0jNr selectable-text copyable-text"]'
        )
        .find_element(by=By.XPATH, value=".//span")
        .text
    )
    return last_msg


if __name__ == "__main__":
    while True:
        if has_unread():
            unread_message = get_last_message()
            response = random.choice(RESPONSES)
            send_message(response)
            driver.refresh()
            time.sleep(15)
        else:
            time.sleep(2)

    # Close the browser
    driver.quit()
