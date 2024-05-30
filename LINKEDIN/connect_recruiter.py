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
from urllib.parse import quote
from time import sleep
from LINKEDIN import constants

home_directory = path.expanduser("~")
local_bin_directory = home_directory + '/bin/'


# input_message = """
# Hi,
# I have a total of 4+ years of experience as full stack engineer.
# Build/scale SaaS products from scratch and contributed to many great products.
# Resume: drive.google.com/file/d/10MltbCkbsKsDQVq56MBeHBwl99fPqsMu/view?usp=drive_link
# Kindly let me know if there are any requirements.
# """


class LinkedinBot():
    def __init__(self, job_profile):
        self.failed = []
        self.success = []
        chrome_options = Options()
        chrome_options.add_argument(
            f"--user-data-dir={local_bin_directory}/chrome-data")
        chrome_options.add_experimental_option("useAutomationExtension", False)

        # options.add_argument('--headless')
        chrome_options.add_argument("--disable-automation")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Adding argument to disable the AutomationControlled flag
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--proxy-server=%s" % PROXY)
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

        service = Service()

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.search_job_profile = f"{job_profile}"
        self.driver.get(
            f"https://www.linkedin.com/search/results/content/?keywords={quote(self.search_job_profile)}&origin=CLUSTER_EXPANSION&sid=._M")
        # https://www.linkedin.com/search/results/content/?keywords={quote(self.search_job_profile)}&origin=CLUSTER_EXPANSION&sid=._M
        # https://www.linkedin.com/search/results/content/?keywords=python%20hiring&origin=CLUSTER_EXPANSION&sid=._M
        sleep(9)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def apply_job(self):
        # open recruiter recommended page on search term
        # list all the items on page
        # send connection on next page with note
        # close the page and repeat

        # global input_message

        list_of_posts = self.driver.find_elements(
            by=By.XPATH,
            value="//div[@class='update-components-actor__meta relative']"
        )
        original_window = self.driver.current_window_handle
        print(f'found {len(list_of_posts)} posts for position: {self.search_job_profile}')
        for index, job in enumerate(list_of_posts):
            try:
                # self.driver._switch_to.window(self.driver.window_handles[1])
                # job.click()
                job_link_url = job.find_element(By.TAG_NAME, "a").get_attribute("href")

                recruiter_name = job.parent.title

                # Define JavaScript to open the link in a new window when clicked
                javascript_code = """
                var linkUrl = arguments[0];
                var newWindow = window.open(linkUrl, '_blank');
                """

                # Execute JavaScript to open the link in a new window when clicked
                self.driver.execute_script(javascript_code, job_link_url)

                sleep(4)
                self.driver._switch_to.window(self.driver.window_handles[1])

                more_button = self.driver.find_elements(
                    by=By.XPATH,
                    value='//*[@aria-label="More actions"]'
                )
                sleep(4)
                more_button[1].click()

                sleep(4)
                # TODO: Add switch statement if connect option is not found in more button then look on main page.
                connect_button = self.driver.find_elements(
                    by=By.XPATH,
                    value="//*[contains(text(),'Connect') and contains(@class,'display-flex t-normal flex-1')]"
                )
                sleep(4)
                connect_button[1].click()

                sleep(4)

                note_button = self.driver.find_element(
                    by=By.XPATH,
                    value='//*[@aria-label="Add a note"]'
                )
                sleep(4)
                note_button.click()

                sleep(4)

                message = self.driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="custom-message"]'
                )
                message.send_keys(constants.LINKEDIN_CANDIDATE_INFO)

                sleep(5)

                invitation = self.driver.find_element(
                    by=By.XPATH,
                    value='//*[@aria-label="Send invitation"]'
                )
                sleep(4)
                invitation.click()
                self.success.append(f'successfully sent message for name: {recruiter_name} url: {job_link_url}')

                sleep(4)
                self.driver.close()
                sleep(4)
                self.driver._switch_to.window(original_window)

            except Exception as e:
                self.failed.append(f'failed to send message for name: {recruiter_name} url: {job_link_url} reason: {e}')
                sleep(4)
                self.driver.close()
                sleep(4)
                self.driver._switch_to.window(original_window)
                # print(f'failed to send message for name: {recruiter_name} \n url: {job_link_url} reason: {e} \n')
        print(self.failed)


if __name__ == '__main__':
    rp = LinkedinBot(job_profile='python hiring')
    rp.apply_job()
