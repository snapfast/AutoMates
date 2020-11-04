
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep
import random



class Angel:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option('excludeSwitches', ["enable-automation"])

        self.driver = webdriver.Chrome(r'/home/nightshade/bin/chromedriver', options=chrome_options)
        self.driver.get("https://angel.co/")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()


aa = Angel()

