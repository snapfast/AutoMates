"""

this file uses local storage folder for browser data

Author: github.com/snapfast

this file applies to Easy Job Recommendations on the Jobs page of Linkedin.

"""

from os import path

from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchElementException
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
        html.send_keys(Keys.END)
        sleep(2)
        html.send_keys(Keys.END)
        sleep(2)
        html.send_keys(Keys.END)
        sleep(10)
        try:
            total_jobs = self.driver.find_elements(by=By.CLASS_NAME, value="jobs-job-board-list__item")
        except NoSuchElementException as xx:
            print(xx, "is not there..")
        print(len(total_jobs))
        num_total_jobs = len(total_jobs)
        original_window = self.driver.current_window_handle
        # cl = random.randint(0, len(easyJobs)-1)
        # cl = total_jobs//2
        cl = 0
        assert len(self.driver.window_handles) == 1
        print('clicking the {} job'.format(cl))
        yehut = True
        while cl < num_total_jobs:
            try:
                try:
                    print(easyJobs[cl].find_element(by=By.CLASS_NAME, value="job-card-container__apply-method"))
                except:
                    print("------------------------------------ Normal job skipping the click")
                    cl += 1
                    continue
                job_name_element = easyJobs[cl].find_element(
                    by=By.CLASS_NAME, value='job-card-list__title') #job-card-container__link
                jname = job_name_element.text
                job_url = job_name_element.get_attribute('href')

                print(jname, job_url)

                cname = easyJobs[cl].find_element(
                    by=By.CLASS_NAME, value='app-aware-link').text

                lname = easyJobs[cl].find_element(
                    by=By.CLASS_NAME, value="job-card-container__metadata-item").text

                with open(r'filename.txt', 'a') as f:
                    print(jname, file=f)
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);", easyJobs[cl])
                action = ActionChains(self.driver)
                # action.move_to_element(job_name_element).key_down(Keys.CONTROL).click(job_name_element).key_up(Keys.CONTROL).perform()
                # action.key_down(Keys.CONTROL).send_keys("t").perform()
                self.driver.switch_to.new_window('tab')
                # .get(easyJobs[cl].get_attribute('href'))
                self.driver._switch_to.window(self.driver.window_handles[1])
                self.driver.get(job_url)
                sleep(2)
                self.apply_job()
                self.driver._switch_to.window(original_window)
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
            # click the resume selector button
            try:
                resume_button = self.driver.find_element(
                    by=By.XPATH, value="//button[@class='artdeco-button artdeco-button--1 artdeco-button--tertiary ember-view']")
                if resume_button.text == "Choose":
                    resume_button.click()
                    print("resume button clicked")
            except:
                pass
            """
            try:
                popup = self.driver.find_element(
                    by=By.CLASS_NAME, value="artdeco-modal--layer-default")
                popup.find_element(
                    by=By.XPATH,
                    value="//label[@for='follow-company-checkbox']")
                print("clicked uncheck")
            except Exception:
                pass
            """
            try:
                self.driver.find_element(by=By.XPATH,
                    value="//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
                print('Next / Submit', cc)
                if cc == 0:
                    # if self.driver.find_element_by_class_name("t-14 fb-form-element-label__title--is-required").text == "City*":
                    #     self.driver.find_element_by_class_name("artdeco-typeahead__input ").send_keys("Ambala, Haryana, India")
                    input(
                        "Please enter appropriate data on web page\n Once entered, press enter/return...")
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



if __name__ == '__main__':
    lo = LinkedinBot()
    lo.click_job()
