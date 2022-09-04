"""

this file uses local storage folder for browser data

Author: github.com/rahbal

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


class NaukriBot:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir={local_bin_directory}/chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option('excludeSwitches', ["enable-automation"])

        service = Service(local_bin_directory + '/chromedriver/chromedriver')

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://www.naukri.com/mnjuser/recommendedjobs")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def click_job(self):
        # jobs = self.driver.find_elements_by_xpath('//*[text()="Easy Apply")]')
        listOfJobs = []
        sleep(10)
        try:
            listOfJobs = self.driver.find_elements(by=By.CLASS_NAME, value="jobTuple")
        except NoSuchElementException as xx:
            print(xx, "JobList not found")
        print(len(listOfJobs))
        # jobs = self.driver.find_elements_by_xpath("//li[contains(text(), 'Easy Apply')]")
        total_jobs = len(listOfJobs)
        original_window = self.driver.current_window_handle
        # cl = random.randint(0, len(easyJobs)-1)
        # cl = total_jobs//2
        cl = 0
        assert len(self.driver.window_handles) == 1
        print('clicking the {} job'.format(cl))
        while cl < total_jobs:
            try:
                job_name_element = listOfJobs[cl]
                job_name_element.click()
                sleep(2)
                # jname = job_name_element.text
                # job_url = job_name_element.get_attribute('href')

                # print(jname, job_url)

                # cname = listOfJobs[cl].find_element(
                #     by=By.CLASS_NAME, value='app-aware-link').text

                # lname = easyJobs[cl].find_element(
                #     by=By.CLASS_NAME, value="job-card-container__metadata-item").text

                # with open(r'filename.txt', 'a') as f:
                #     print(jname, file=f)
                # self.driver.execute_script(
                #     "arguments[0].scrollIntoView(true);", easyJobs[cl])
                action = ActionChains(self.driver)
                # action.move_to_element(job_name_element).key_down(Keys.CONTROL).click(job_name_element).key_up(Keys.CONTROL).perform()
                # action.key_down(Keys.CONTROL).send_keys("t").perform()
                # self.driver.switch_to.new_window('tab')
                # .get(easyJobs[cl].get_attribute('href'))
                self.driver._switch_to.window(self.driver.window_handles[1])
                applyContainer = self.driver.find_element(by=By.CLASS_NAME,value='apply-button-container')
                applyContainer.find_element(by=By.CLASS_NAME,value='apply-button').click()
                sleep(2)
                self.driver.close()
                self.driver._switch_to.window(original_window)
                cl += 1
            except ElementNotInteractableException:
                print('scroll a bit please, cannot see the element yet')
                sleep(2)
        sleep(2)


if __name__ == '__main__':
    lo = NaukriBot()
    lo.click_job()
