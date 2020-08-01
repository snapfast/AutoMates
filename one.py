from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from secrets import pw


class LinkedinBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome('D:\libtools\chromedriver\chromedriver.exe')
        self.username = username
        self.driver.get("https://linkedin.com/login")
        sleep(2)
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/jobs')]")\
            .click()
        sleep(2)

    def go_jobs(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/feed')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/jobs')]")\
            .click()
        sleep(2)

    def apply_job(self):
        self.driver.find_element_by_class_name('jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view').click()
        sleep(2)
        self.driver.find_element_by_class_name('artdeco-button artdeco-button--2 artdeco-button--primary ember-view').click()
        sleep(1)

    def click_job_card(self):
        # jobs = self.driver.find_elements_by_xpath('//*[text()="Easy Apply")]')
        xx = 0
        easyJobs = []
        while len(easyJobs) == 0:
            try:
                easyJobs = self.driver.find_elements_by_xpath("//*[text()='Easy Apply']/ancestor::*[@class='ember-view job-card-square__link display-flex flex-grow-1 flex-column align-items-stretch full-width js-focusable-card']")
            except NoSuchElementException:
                print(xx, 'is not there..')
            print(easyJobs)
            xx += 1
        # jobs = self.driver.find_elements_by_xpath("//li[contains(text(), 'Easy Apply')]")
        print(easyJobs, type(easyJobs))
        easyJobs[0].click()
        sleep(2)

    def check_job_card(self): # checks if there are any job cards on the page.
        try:
            card_list = self.driver.find_element_by_class_name("job-card-square__link").click()
        except NoSuchElementException:
            print("selenium.common.exceptions.NoSuchElementException")
            card_list = []
        print(card_list)
        return len(card_list)

    def _get_names(self):
        print('hello')


Lbot = LinkedinBot('rahulbali.mecse16@pec.edu.in', pw)
Lbot.click_job_card()
Lbot.apply_job()
