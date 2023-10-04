from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = "Your username"  # Change it to your account username
PASSWORD = "Your password"  # Change it to your account password
URL = "https://www.instagram.com/accounts/login/"


class Login:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def login_to_insta(self) -> None:
        self.driver.get(URL)
        time.sleep(6)
        self.user_id = self.driver.find_element(By.NAME, "username")
        self.user_id.send_keys(USERNAME)
        self.pass_ = self.driver.find_element(By.NAME, "password")
        self.pass_.send_keys(PASSWORD)

        self.enter_button = self.driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'
        )
        self.enter_button.click()

        self.not_now_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._ac8f div"))
        )
        self.not_now_button.click()

    def follower_bot(self, similar_account: str):
        self.driver.get(f"https://www.instagram.com/{similar_account}/")
        self.driver.get(f"https://www.instagram.com/{similar_account}/followers/")

        self.dialog = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_aano"))
        )
        self.start = 0
        try:
            while True:
                f_buttons = self.driver.find_elements(
                    By.CSS_SELECTOR, "div._aano button._acan._acap._acas._aj1-"
                )
                self.length = len(f_buttons)
                for i in range(self.start, self.length):
                    try:
                        button = f_buttons[i]
                        button.click()
                        time.sleep(2)
                    except:
                        pass
                self.start = self.length
                self.driver.execute_script("arguments[0].scrollBy(0, 100)", self.dialog)
                time.sleep(2)
        except Exception as e:
            pass


accounts_to_follow = [
    "unstop.world",
    "scienmanas",
]  # Update which all accounts you want to follow

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)  # Chrome Web driver

loginn = Login(driver)
loginn.login_to_insta()
for account in accounts_to_follow:
    loginn.follower_bot(account)

driver.quit()
