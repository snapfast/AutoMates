
# this file uses local storage folder for browser data
# login to the account before executing the actual script
from os import path, mkdir, remove, chmod
import sys
from urllib import request
import json
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
local_bin_directory = home_directory + '/bin'

# change this url to correct version of the chrome installed on your system
# get the chrome version > Chrome > About Chrome < Copy Paste that number here.

distribution = {
    "linux": "linux64",
    "mac_intel": "mac-x64",
    "mac_arm": "mac-arm64",
    "win32": "win32",
    "win64": "win64",
}

# setup chromedriver before any execution
def setupCD(os_type):

    # updated mechanism as written in the https://chromedriver.chromium.org/#h.8cjh6c3ay1qq
    json_url = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json'

    # store the response of URL
    response = request.urlopen(json_url)
    
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    platforms = data_json['channels']['Stable']['downloads']['chromedriver']
    LATEST_RELEASE = data_json['channels']['Stable']['version']

    for x in platforms:
        if x['platform'] == os_type:
            url = x['url']

    print('Chrome Driver version installed: ', LATEST_RELEASE)
    print('Downloading from ', url)
    print(os_type)

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
        zip22.extract('chromedriver', local_bin_directory + '/chromedriver')
        zip22.close()
        remove(local_bin_directory + fileName)
        if os_type != 'win32' or os_type != 'win64': #do not change the permission if it is windows
            chmod(local_bin_directory + '/chromedriver', 0o744)
        print("chromedriver installed.")


def loginWindow():
    print(local_bin_directory)
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={local_bin_directory}/chrome-data")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_experimental_option('excludeSwitches',
    # ["enable-automation"])

    service = Service()
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
        rmtree(local_bin_directory + "/chromedriver")
    except:
        print("reset failed, manually delete files in " + local_bin_directory + "/chromedriver")

