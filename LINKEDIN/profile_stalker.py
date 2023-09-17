import random
from os import path
from sys import argv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep

home_directory = path.expanduser("~")
local_bin_directory = home_directory + '/bin/'


class LinkedinBot():

    def __init__(self, any_profile_link):
        # term = self.term
        self.page_number = 5
        chrome_options = Options()
        chrome_options.add_argument(
            f"--user-data-dir={local_bin_directory}/chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)

        service = Service()

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get(any_profile_link)
        sleep(10)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def stalk_on(self):

        html = self.driver.find_element(by=By.TAG_NAME, value='html')


        while 1:
            info = self.driver.find_elements(
                by=By.CLASS_NAME, value="pv-text-details__left-panel")
            
            print(info[0].text)
            print(info[1].text)

            sleep(5)
            j = random.randrange(0, 10, 2)
            # sleep(5)
            # html.send_keys(Keys.PAGE_DOWN)

            # click one of the 5 profiles profiles on the right side
            try:
                side_profiles = self.driver.find_elements(
                    by=By.XPATH, value="//a[@data-field='browsemap_card_click']")
                # print(len(side_profiles), j, side_profiles)

                file = open("filename.txt", "w")
                print("-------------------", j, len(side_profiles), file=file, end="\n")
                file.close()

                
                side_profiles[j].click()
            except NoSuchElementException as NoSuch:
                print(NoSuch, "\n cool")
            sleep(5)


if __name__ == '__main__':
    position = argv[1]
    location = argv[2]

    lb = LinkedinBot()
    lb.connect()
