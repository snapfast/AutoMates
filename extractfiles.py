from os import path, mkdir, remove
from urllib import request
from zipfile import ZipFile
from time import sleep

chromedriver = 'chromedriver/chromedriver.exe'
url = 'https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_win32.zip'

## setup chromedriver before any execution
def setupCD(url):
    if path.isfile(chromedriver):
        print('chromedriver correctly installed')
        return 0
    try:
        mkdir('chromedriver')
        request.urlretrieve(url, 'chromedriver/chromedriver_win32.zip')
        print('downloading the chromedriver...')
        sleep(30)
    except FileExistsError as err:
        print('chromedriver already downloaded')
    zip22 = ZipFile('chromedriver/chromedriver_win32.zip', 'r')
    zip22.namelist()
    zip22.extractall('chromedriver')
    zip22.close()
    remove('chromedriver/chromedriver_win32.zip')
    print("chromedriver installed.")

setupCD(url)