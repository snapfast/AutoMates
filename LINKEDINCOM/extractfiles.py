from os import *
from urllib import request
from zipfile import ZipFile
from time import sleep


home_directory = path.expanduser("~")
local_binary_directory = home_directory + '/bin/'

# change this url to correct version of the chrome installed on your system
# get the chrome version > Chrome > About Chrome < Copy Paste that number here.
url = 'https://chromedriver.storage.googleapis.com/\
103.0.5060.53/chromedriver_linux64.zip'


# setup chromedriver before any execution
def setupCD(url):

    # get filename from the URL
    url_tokens = url.split("/")
    fileName = url_tokens[-1]

    # if the Binary folder does not exists, Create
    if not path.isdir(local_binary_directory):
        mkdir(local_binary_directory)

    # check if chromedriver exist, if not download and extract
    if path.isdir(local_binary_directory + '/chromedriver'):
        print('chromedriver correctly installed')
        return 0
    else:
        try:
            request.urlretrieve(url, local_binary_directory + fileName)
            print('downloading the chromedriver...')
            sleep(30)
        except FileExistsError as err:
            print('chromedriver already downloaded', err)
        zip22 = ZipFile(local_binary_directory + fileName, 'r')
        zip22.namelist()
        zip22.extractall(local_binary_directory + '/chromedriver')
        zip22.close()
        remove(local_binary_directory + fileName)
        chmod(local_binary_directory + '/chromedriver/', 0o744)
        print("chromedriver installed.")


setupCD(url)
