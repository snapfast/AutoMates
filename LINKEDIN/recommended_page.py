from os import path
from sys import argv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import ElementNotInteractableException
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep

home_directory = path.expanduser("~")
local_bin_directory = home_directory + '/bin/'


class LinkedinBot():

    def __init__(self):
        # term = self.term
        self.page_number = 5

        chrome_options = Options()
        chrome_options.add_argument(
            f"--user-data-dir={local_bin_directory}/chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)

        service = Service()

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://www.linkedin.com/jobs/recommended/")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def change_page(self):
        # get the current page number, self.page_number
        # then find that page number element, then click the element
        self.page_number += 1
        try:
            next_page_list_item = self.driver.find_element(
                by=By.XPATH,
                value=f"//li[@data-test-pagination-page-btn='{self.page_number}']")
            print(next_page_list_item)
            print(next_page_list_item.get_attribute("class"))
            next_page_button = next_page_list_item.find_element(by=By.TAG_NAME,
                                                                value='button')
            print(next_page_button)
            print(next_page_button.get_attribute('aria-label'))
            next_page_button.click()
        except NoSuchElementException as NoSuch:
            print(NoSuch, "\n cool enough")

    def click_easy_jobs(self):

        while 1:
            # left panel jobs
            try:
                left_panel_jobs = self.driver.find_elements(
                    by=By.CLASS_NAME, value="jobs-search-results__list-item")
                print(left_panel_jobs)
            except NoSuchElementException as NoSuch:
                print(NoSuch, "\n cool")

            total_jobs = len(left_panel_jobs)
            print(total_jobs, left_panel_jobs)

            # storing the main tab context
            original_window = self.driver.current_window_handle
            j = 0
            # looping on each left panel job one by one.
            while j < total_jobs:
                sleep(2)
                try:
                    job_name_element = left_panel_jobs[j].find_element(
                        by=By.CLASS_NAME, value='job-card-list__title')
                    print(job_name_element)
                    # company_name_element = left_panel_jobs[j].find_element(
                    #     by=By.CLASS_NAME, value='job-card-container__company-name')
                    # location_element = left_panel_jobs[j].find_element(
                    #     by=By.CLASS_NAME,
                    #     value='job-card-container__metadata-wrapper')
                    jname = job_name_element.text
                    # cname = company_name_element.text
                    # lname = location_element.text
                    job_url = job_name_element.get_attribute('href')

                    with open(r'filename.txt', 'a') as f:
                        print(jname, file=f)
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView(true);", left_panel_jobs[j])
                    self.driver.switch_to.new_window('tab')
                    self.driver._switch_to.window(
                        self.driver.window_handles[1])
                    self.driver.get(job_url)
                    sleep(2)
                    self.apply_job()
                    self.driver._switch_to.window(original_window)
                    j += 1
                except ElementNotInteractableException:
                    print('scroll a bit please, cannot see the element yet')
                    sleep(2)
            self.change_page()

    def apply_job(self):
        # Section to click the Easy Apply Button on job page
        gerat = True
        while gerat:
            try:
                self.driver.find_element(
                    by=By.XPATH,
                    value="//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']"
                ).click()
                print('Clicked the Easy Button')
                gerat = False
            except NoSuchElementException:
                print('Cannot find the button, click Another Job')
                break
            except NoSuchWindowException as win:
                print("no window bro... ok, I believe you closed it.", win)
                gerat = False
        sleep(2)

        gerat = True
        cc = 5
        while gerat:
            # try:
            #     checkbox = self.driver.find_element(
            #         by=By.CLASS_NAME, value="ember-checkbox")
            #     self.driver.execute_script(
            #         "arguments[0].scrollIntoView(true);", checkbox)
            #     checkbox.click()
            #     print("clicked checkbox")
            # except Exception as e:
            #     print(e, "no checkbox")

            # find the element for selecting resume
            try:
                resume_button = self.driver.find_element(
                    by=By.XPATH, value="//button[@class='artdeco-button artdeco-button--1 artdeco-button--tertiary ember-view']")
                if resume_button.text == "Choose":
                    resume_button.click()
                    print("resume button clicked")
            except:
                pass
            try:
                self.driver.find_element(
                    by=By.XPATH,
                    value="//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']"
                ).click()
                print('Next / Submit', cc)
                if cc == 0:
                    input("Please enter appropriate data on web page")
                    cc = 5
                cc -= 1
                sleep(3)
            except NoSuchElementException:
                gerat = False
            except NoSuchWindowException as win:
                print("no window bro... ok, I believe you closed it.", win)
                gerat = False
        print("job applied")
        try:
            self.driver.close()
        except NoSuchWindowException as ns:
            print(ns, "window might have been closed by user.")


if __name__ == '__main__':

    rp = LinkedinBot()
    rp.click_easy_jobs()
    rp.change_page()
