from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep
import random


class LinkedinBot():
    def __init__(self):
        # term = self.term
        # country = self.country
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option('excludeSwitches', ["enable-automation"])

        self.driver = webdriver.Chrome('/home/nightshade/bin/chromedriver', options=chrome_options)
        self.driver.get("https://linkedin.com/jobs")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def do_search(self):
        sleep(2)
        box = self.driver.find_elements_by_class_name("jobs-search-box__text-input")
        # print(box, len(box))
        box[0].send_keys("site reliability engineer")
        box[2].send_keys("India")
        sleep(5)
        self.driver.find_element_by_xpath("//button[text()='Search']").click()

    def click_easy_jobs(self):
        sleep(30)
        try:
            easyJobs = self.driver.find_elements_by_xpath("//*[text()='Easy Apply']/ancestor::*[@class='jobs-search-results__list list-style-none']")
        except NoSuchElementException as NoSuch:
            print(NoSuch, "\n cool")
        print(len(easyJobs))
        gather_jobs = self.driver.find_elements_by_class_name("jobs-search-results__list-item")
        ## brings total number of jobs out of the main job search page , actually no need in this file.
        for onejob in range(200):
            # Section to click the Easy Apply Button on job page
            # Real work starts here
            # Now we click each job in the left column, based on the total jobs on each page
            # simply click to start
            print(onejob, gather_jobs)
            gather_jobs[onejob].click()
            gerat = True
            while 1:
                # check if job already applied
                sleep(6)
                try:
                    self.driver.find_element_by_xpath("//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
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
                    self.driver.find_element_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()
                    print('Next / Submit')
                    if cc == 0:
                        input("please enter appropriate data on web page, then press any key here...")
                        cc = 5
                    cc -= 1
                    sleep(2)
                except NoSuchElementException:
                    gerat = False
            print("job applied")
            self.driver.find_element_by_class_name("artdeco-modal__dismiss").click()

gg = LinkedinBot()
gg.do_search()
# gg.scroll_jobs()
gg.click_easy_jobs()
