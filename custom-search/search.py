
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

        self.driver = webdriver.Chrome(
            r'chromedriver\chromedriver.exe', options=chrome_options)
        self.driver.get("https://linkedin.com/jobs")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def do_search(self):
        sleep(2)
        box = self.driver.find_elements_by_class_name("jobs-search-box__text-input")
        print(box, len(box))
        box[0].send_keys("linux administrator")
        box[2].send_keys("India")
        sleep(5)
        self.driver.find_element_by_xpath("//button[text()='Search']").click()

    def scroll_jobs(self):
        sleep(2)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        sleep(2)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        sleep(2)

    def click_easy_jobs(self):
        sleep(15)
        try:
            easyJobs = self.driver.find_elements_by_xpath("//*[text()='Easy Apply']/ancestor::*[@class='jobs-search-results__list list-style-none']")
        except NoSuchElementException as NoSuch:
            print(NoSuch, "\n cool")
        print(len(easyJobs))
        for onejob in range(200):
            # Section to click the Easy Apply Button on job page
            gerat = True
            while gerat:
                try:
                    self.driver.find_element_by_xpath("//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
                    print('Clicked the Easy Button')
                    gerat = False
                except NoSuchElementException:
                    print('Cannot find the button, click Another Job')
                    sleep(6)
            sleep(2)

            gerat = True
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

gg = LinkedinBot()
gg.do_search()
# gg.scroll_jobs()
gg.click_easy_jobs()