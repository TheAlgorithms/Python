from selenium import webdriver
from selenium.webdriver.common.by import By


class BankDetails:
    def __init__(self, ifsc_code) -> None:
        # Initialize the Chrome web driver.
        self.driver = webdriver.Chrome()
        self.URL = "https://www.ifsccodebank.com/search-by-IFSC-code.aspx"
        self.ifsc_code = ifsc_code

    def request_ifsc(self) -> str:
        try:
            # Navigate to the website.
            self.driver.get(self.URL)

            # Locate the input element to enter the IFSC code.
            input_ele = self.driver.find_element(By.XPATH, '//*[@id="txtIFSCCode"]')

            # Enter the IFSC code.
            input_ele.send_keys(self.ifsc_code)

            # Find and submit the search button.
            submit_btn = input_ele.find_element(By.XPATH, '//*[@id="BC_btnSeach"]')
            submit_btn.submit()

            # Check if details were found or not.
            is_details_valid = self.driver.find_element(
                By.XPATH, '//*[@id="BC_GV"]/tbody/tr/td/div'
            ).text

            if is_details_valid == "There are currently no items found.":
                return "Details not found"
            else:
                return "Details Found"
        except AttributeError:
            return "Details not found"

    def get_bank_details(self) -> dict:
        # Locate and extract various details on the page.
        ifsc_code = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[1]/table/tbody/tr[1]/td[2]/div[1]/div[1]/a',
        )

        bank = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[1]/table/tbody/tr[2]/td[2]/b',
        )

        branch = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[1]/table/tbody/tr[3]/td[2]/a',
        )

        business_hours = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[1]/table/tbody/tr[4]/td[2]/time',
        )

        mode_of_payment = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[1]/table/tbody/tr[5]/td[2]',
        )

        contact = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[1]/table/tbody/tr[6]/td[2]',
        )

        bank_details = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[1]/table/tbody/tr[7]/td[2]',
        )

        remittance_service = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[2]/div/table/tbody/tr[1]/td[2]',
        )

        location = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[2]/div/table/tbody/tr[2]/td[2]',
        )

        city = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/a',
        )

        district = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[2]/div/table/tbody/tr[4]/td[2]/a',
        )

        pincode = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[2]/div/table/tbody/tr[6]/td[2]',
        )

        country = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[2]/div/table/tbody/tr[7]/td[2]',
        )

        address = self.driver.find_element(
            By.XPATH,
            '//*[@id="BC_GV"]/tbody/tr/td/div[1]/div[2]/div/table/tbody/tr[8]/td[2]',
        )

        # Create a dictionary with the extracted information.
        return {
            "IFSC Code": ifsc_code.text,
            "Bank": bank.text,
            "Branch": branch.text,
            "Business Hours": business_hours.text,
            "Mode of Payment": mode_of_payment.text,
            "Contact": contact.text,
            "Bank Details : ": bank_details.text,
            "Remittance Service": remittance_service.text,
            "Location": location.text,
            "City": city.text,
            "District": district.text,
            "Pincode": pincode.text,
            "Country": country.text,
            "Address": address.text,
        }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    ifsc_code = "<YOUR_IFSC_CODE>"

    # Check the length of the provided IFSC code.
    if len(ifsc_code) == 11:
        obj = BankDetails(ifsc_code)
        request_code = obj.request_ifsc()

        if request_code == "Details Found":
            bank_details = obj.get_bank_details()

            # Print the extracted bank details.
            print(bank_details)
        else:
            print("Details not found")
    else:
        print("Invalid Code")
