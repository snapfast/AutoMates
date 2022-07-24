# this file uses local storage folder for browser data
# login to the account before executing the actual script
from os import path

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import random
from time import sleep

home_directory = path.expanduser("~")
local_bin_directory = home_directory + '/bin/'


class BumbleBot:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir={local_bin_directory}/chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option('excludeSwitches', ["enable-automation"])

        service = Service(local_bin_directory + '/chromedriver/chromedriver')

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://bumble.com/app")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def right_swipe(self):
        sleep(2)
        while 1:
            sleep(random.randint(3, 13))
            try:
                like = self.driver.find_element(
                    by=By.CLASS_NAME, value="encounters-action--like")
            except NoSuchElementException as xx:
                print(xx, "is not there..")
            like.click()


b = BumbleBot()
b.right_swipe()
