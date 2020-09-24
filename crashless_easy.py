
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep
import random

from selenium.webdriver.chrome.options import Options


class LinkedinBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        # chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option('excludeSwitches', ["enable-automation"])

        self.driver = webdriver.Chrome('D:\libtools\chromedriver\chromedriver.exe', options=chrome_options)
        self.driver.get("https://linkedin.com/jobs")
        sleep(2)


Lbot = LinkedinBot()
