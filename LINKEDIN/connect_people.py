from os import path
from sys import argv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from functools import reduce
from selenium.webdriver.chrome.service import Service

from time import sleep
from random import randint

home_directory = path.expanduser("~")
local_bin_directory = home_directory + '/bin/'


class LinkedinBot():

    def __init__(self, company_name):
        # term = self.term
        self.page_number = 5
        chrome_options = Options()
        chrome_options.add_argument(
            f"--user-data-dir={local_bin_directory}/chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)

        service = Service()

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get(
            f"https://www.linkedin.com/company/{company_name}/people/")
        sleep(10)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def connect(self):

        html = self.driver.find_element(by=By.TAG_NAME, value='html')
        j = 0
        total_jobs = 0

        while 1:
            if total_jobs < 200:
                html.send_keys(Keys.END)
                sleep(1)
                # left panel jobs
                try:
                    visible_buttons = self.driver.find_elements(
                        by=By.XPATH, value="//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view full-width']")
                except NoSuchElementException as NoSuch:
                    print(NoSuch, "\n cool")
            else:
                j += 1

            # visible_connect_buttons = reduce(check_connect_text ,visible_buttons, [])
            total_jobs = len(visible_buttons)
            print(total_jobs, j)

            try:
                self.driver.execute_script(
                    "window.scrollTo(0, arguments[0].offsetTop);", visible_buttons[j])
                if visible_buttons[j].text == "Connect":
                    job_name_element = visible_buttons[j].click()
                else:
                    print(visible_buttons[j].text)
                    continue

                print(job_name_element)

                sleep(randint(3, 8))

                send_button = self.driver.find_element(
                    by=By.XPATH, value="//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml1']")
                send_button.click()
            except ElementNotInteractableException:
                print('scroll a bit please, cannot see the element yet')
                sleep(2)
            except NoSuchElementException:
                print('asking for person email for connect, clicking X, move to next')
                self.driver.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Dismiss"]').click()


def check_connect_text(first, second):
    return [first, second]


if __name__ == '__main__':
    position = argv[1]
    location = argv[2]

    lb = LinkedinBot()
    lb.connect()
