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
        # country = self.country
        chrome_options = Options()
        chrome_options.add_argument(
            f"--user-data-dir={local_bin_directory}/chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)

        service = Service(local_bin_directory + '/chromedriver/chromedriver')

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://linkedin.com/jobs")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def do_search(self):
        box = self.driver.find_elements(
            by=By.CLASS_NAME, value="jobs-search-box__text-input")
        box[0].click()
        sleep(1)
        box[0].send_keys(argv[1])  # job title
        box[3].send_keys("Japan\n")  # location

    def click_easy_jobs(self):
        sleep(5)

        # turn on filter for the Easy Apply Jobs, all jobs will be easy ones
        easy_apply_filter_parent = self.driver.find_element(
            by=By.CLASS_NAME, value='search-reusables__filter-binary-toggle')

        easy_apply_filter_parent.find_element(
            by=By.TAG_NAME, value='button').click()

        print(easy_apply_filter_parent.text)
        sleep(2)

        # left panel jobs
        try:
            left_panel_jobs = self.driver.find_elements(
                by=By.CLASS_NAME, value="jobs-search-results__list-item")
        except NoSuchElementException as NoSuch:
            print(NoSuch, "\n cool")
        print(len(left_panel_jobs))

        # storing the main tab context
        original_window = self.driver.current_window_handle
        jj = 0

        # looping on each left panel job one by one.
        while 1:
            sleep(2)
            one_job = left_panel_jobs[jj]
            try:
                job_name_element = one_job.find_element(
                    by=By.CLASS_NAME, value='job-card-list__title')
                jname = job_name_element.text
                job_url = job_name_element.get_attribute('href')
                print(jname, job_url)

                with open(r'filename.txt', 'a') as f:
                    print(jname, file=f)
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);", one_job)
                self.driver.switch_to.new_window('tab')
                self.driver._switch_to.window(self.driver.window_handles[1])
                self.driver.get(job_url)
                sleep(2)
                self.apply_job()
                self.driver._switch_to.window(original_window)
                jj += 1
            except ElementNotInteractableException:
                print('scroll a bit please, cannot see the element yet')
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
                break
            except NoSuchWindowException as win:
                print("no window bro... ok, I believe you closed it.", win)
                gerat = False
        sleep(2)

        gerat = True
        cc = 5
        while gerat:
            try:
                checkbox = self.driver.find_element(
                    by=By.CLASS_NAME, value="ember-checkbox")
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);", checkbox)
                checkbox.click()
                print("clicked checkbox")
            except Exception as e:
                print(e, "no checkbox")
            try:
                self.driver.find_element(by=By.XPATH,
                    value="//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
                print('Next / Submit', cc)
                if cc == 0:
                    input("Please enter appropriate data on web page")
                    cc = 5
                cc -= 1
                sleep(2)
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


lb = LinkedinBot()
lb.do_search()
lb.click_easy_jobs()

