from os import *

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep
import random

home_directory = path.expanduser("~")
local_bin_directory = home_directory + '/bin/'


class LinkedinBot():
    def __init__(self):
        # term = self.term
        # country = self.country
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir={local_bin_directory}/chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option('excludeSwitches', ["enable-automation"])

        service = Service(local_bin_directory + '/chromedriver/chromedriver')

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://linkedin.com/jobs")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def do_search(self):
        box = self.driver.find_elements(by=By.CLASS_NAME, value="jobs-search-box__text-input")
        print(box, len(box))
        box[0].click()
        sleep(1)
        box[0].send_keys("site reliability engineer")
        box[3].send_keys("Australia\n")

        # submit = self.driver.find_element(by=By.CLASS_NAME, value="jobs-search-box__submit-button")
        # submit.click()
        # ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def click_easy_jobs(self):
        sleep(15)
        try:
            left_panel_jobs = self.driver.find_elements(by=By.CLASS_NAME,value="jobs-search-results__list-item")
            # easyJobs = self.driver.find_elements(by=By.XPATH, value="//*[text()='Easy Apply']/ancestor::*[@class='jobs-search-results__list-item']")
        except NoSuchElementException as NoSuch:
            print(NoSuch, "\n cool")
        print(len(left_panel_jobs))
        for onejob in left_panel_jobs:
            try:
                easyJob = onejob.find_element(by=By.LINK_TEXT, value="Easy Apply")
            except Exception as e:
                raise e
            if easyJob:
                try:
                    onejob.click()
                except Exception as e:
                    raise e
                gerat = True
                while 1:
                    # check if job already applied
                    sleep(6)
                    try:
                        self.driver.find_element(by=By.XPATH, value="//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
                        print('Clicked the Easy Button')
                        break
                    except NoSuchElementException:
                        print('Cannot find the button, automatically clicking NEXT Job')
                        gerat = False
                        sleep(6)
                sleep(2)

                cc = 5
                while gerat:
                    try:
                        try:
                            self.driver.find_element(by=By.ID, value="follow-company-checkbox").click()
                            print("unchecked")
                        except Exception as e:
                            print(e, "no checkbox")
                        self.driver.find_element(by=By.XPATH, value="//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary']").click()
                        print('Next / Submit')
                        if cc == 0:
                            input("please enter appropriate data on web page, then press any key here...")
                            cc = 5
                        cc -= 1
                        sleep(2)
                    except NoSuchElementException:
                        gerat = False
                print("job applied")


gg = LinkedinBot()
gg.do_search()
# gg.scroll_jobs()
try:
    gg.click_easy_jobs()
except Exception:
    gg.driver.close()
