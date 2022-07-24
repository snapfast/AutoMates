# this file uses local storage folder for browser data
# login to the account before executing the actual script
from os import *

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep
import random

home_directory = path.expanduser("~")
local_bin_directory = home_directory + '/bin/'


class LinkedinBot:

    def __init__(self):
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

    def click_job(self):
        # jobs = self.driver.find_elements_by_xpath('//*[text()="Easy Apply")]')
        easyJobs = []
        sleep(2)
        html = self.driver.find_element(by=By.TAG_NAME, value='html')
        html.send_keys(Keys.END)
        sleep(2)
        html = self.driver.find_element(by=By.TAG_NAME, value='html')
        html.send_keys(Keys.END)
        sleep(10)
        while len(easyJobs) == 0:
            try:
                easyJobs = self.driver.find_element(by=By.XPATH, value="//*[text()='Easy Apply']/ancestor::*[@class='ember-view job-card-square__link display-flex flex-grow-1 flex-column align-items-stretch full-width js-focusable-card']")
            except NoSuchElementException as xx:
                print(xx, "is not there..")
            print(len(easyJobs))
        # jobs = self.driver.find_elements_by_xpath("//li[contains(text(), 'Easy Apply')]")
        total_jobs = len(easyJobs)
        original_window = self.driver.current_window_handle
        # cl = random.randint(0, len(easyJobs)-1)
        # cl = total_jobs//2
        cl = 0
        assert len(self.driver.window_handles) == 1
        print('clicking the {} job'.format(cl))
        yehut = True
        while cl < total_jobs:
            try:
                jname = easyJobs[cl].find_element_by_class_name(
                    'job-card-square__title').text
                '''
                cname = easyJobs[cl].find_element_by_class_name(
                    'job-card-container__company-name').text
                lname = easyJobs[cl].find_element_by_css_selector(
                    "li[data-test-job-card-square__location]").text
                '''
                with open(r'filename.txt', 'a') as f:
                    print(jname, file=f)
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);", easyJobs[cl])
                action = ActionChains(self.driver)
                action.key_down(Keys.CONTROL).click(easyJobs[cl]).key_up(Keys.CONTROL).perform()
                # self.driver.switch_to.new_window('tab')
                # .get(easyJobs[cl].get_attribute('href'))
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.apply_job()
                self.driver.switch_to.window(original_window)
                cl += 1
            except ElementNotInteractableException:
                print('scroll a bit please, cannot see the element yet')
                sleep(2)
        sleep(2)

    def apply_job(self):
        # Section to click the Easy Apply Button on job page
        gerat = True
        while gerat:
            try:
                self.driver.find_element(by=By.XPATH,
                    value="//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
                print('Clicked the Easy Button')
                gerat = False
            except NoSuchElementException:
                print('Cannot find the button, click Another Job')
                sleep(6)
            except NoSuchWindowException as win:
                print("no window bro... ok, I believe you closed it.")
                gerat = False
        sleep(2)

        gerat = True
        cc = 5
        while gerat:
            try:
                self.driver.find_element(by=By.XPATH,
                    value="//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
                print('Next / Submit', cc)
                if cc == 0:
                    # if self.driver.find_element_by_class_name("t-14 fb-form-element-label__title--is-required").text == "City*":
                    #     self.driver.find_element_by_class_name("artdeco-typeahead__input ").send_keys("Ambala, Haryana, India")
                    input(
                        "please enter appropriate data on web page, then press any key here...")
                    cc = 5
                cc -= 1
                sleep(2)
            except NoSuchElementException:
                gerat = False
            except NoSuchWindowException as win:
                print("no window bro... ok, I believe you closed it.")
                gerat = False
        print("job applied")
        try:
            self.driver.close()
        except NoSuchWindowException as ns:
            print(ns, "window might have been closed by usre Rahul Bali.")


lo = LinkedinBot()
lo.click_job()
lo.go_exit()
