
# this file uses local storage folder for browser data
# login to the account before executing the actual script
from os import path, mkdir, remove, chmod
import sys
from urllib import request
from zipfile import ZipFile
from time import sleep
from shutil import rmtree


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

home_directory = path.expanduser("~")
local_bin_directory = home_directory + '/bin/'

stable_release_version_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'

# change this url to correct version of the chrome installed on your system
# get the chrome version > Chrome > About Chrome < Copy Paste that number here.

distribution = {
    "linux": "linux64",
    "mac": "mac64",
    "mac_m1": "mac64_m1",
    "win": "win32",
}

# setup chromedriver before any execution
def setupCD(os_type):

    LATEST_RELEASE = request.urlopen(stable_release_version_url).read().decode('utf-8')

    print('Chrome version installed: ', LATEST_RELEASE)

    url = f'https://chromedriver.storage.googleapis.com/{LATEST_RELEASE}/chromedriver_{distribution[os_type]}.zip'

    # get filename from the URL
    url_tokens = url.split("/")
    fileName = url_tokens[-1]

    # if the Binary folder does not exists, Create
    if not path.isdir(local_bin_directory):
        mkdir(local_bin_directory)

    # check if chromedriver exist, if not download and extract
    if path.isdir(local_bin_directory + '/chromedriver'):
        print('chromedriver correctly installed')
        return 0
    else:
        try:
            request.urlretrieve(url, local_bin_directory + fileName)
            print('downloading the chromedriver...')
            sleep(30)
        except FileExistsError as err:
            print('chromedriver already downloaded', err)
        zip22 = ZipFile(local_bin_directory + fileName, 'r')
        zip22.namelist()
        zip22.extractall(local_bin_directory + '/chromedriver')
        zip22.close()
        remove(local_bin_directory + fileName)
        if os_type != 'win': #do not change the permission if it is windows
            chmod(local_bin_directory + '/chromedriver/chromedriver', 0o744)
        print("chromedriver installed.")


def loginWindow():
    print(local_bin_directory)
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={local_bin_directory}/chrome-data")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_experimental_option('excludeSwitches',
    # ["enable-automation"])

    service = Service(local_bin_directory + '/chromedriver/chromedriver')
    driver = None

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except SessionNotCreatedException:
        print("Update your chrome to latest version, then run again. Also, try to Reset the Setup.")
        sys.exit()
    driver.get("https://linkedin.com/")
      
    # second tab
    driver.execute_script("window.open('about:blank', 'secondtab');")
    driver.switch_to.window("secondtab")
      
    # In the second tab
    driver.get('https://naukri.com/')
    sleep(120)
    driver.close()
    driver.quit()


def reset():
    try:
        rmtree(local_bin_directory + "chromedriver")
    except:
        print("reset failed, manually delete files in " + local_bin_directory + "chromedriver")

