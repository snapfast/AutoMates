# AutoMates
Automate the finding people/jobs on Apps like LinkedIn, Bumble, AngelList.


## Setup (Ubuntu)

Run the  command to install the only package needed `selenium`.  

- `sudo apt install python3-selenium`
- `git clone https://github.com/snapfast/AutoMates`
- `cd Automates`
- `python run.py`
- Just use the menu to do things.

This program is only supported on Python 3.10 and above.

## Usage

run.py

## Usage screenshots (Deprecated by New Selenium Manager)

Since the release of selenium manager, chrome, firefox and safari drivers are automatically configured by selenium.   
Read more here https://www.selenium.dev/blog/2022/introducing-selenium-manager/

![Usage](./zz/Screenshot_from_2022-09-13_22-34-19_1.png)

## Usage (deprecated)

To run for specific website, choose from below commands.

### Linkedin
```python
python LINKEDIN/recommended_jobs.py  # to apply for recommended jobs in Jobs Section
python LINKEDIN/search_jobs.py "software engineer" gurgaon  # to search for jobs per location
```
### Naukari
```python
python NAUKRI/recommended_jobs.py  # to apply for recommended jobs in Jobs Section
python NAUKRI/search_jobs.py "angular developer" bangalore  # to search for jobs per location
```

### Bumble
```python
python BUMBLE/swipe.py # just right swipe only, it does a right swipe on random time, 3 secs to 13 secs.
```

### Angel List
TBD


__NOTE: RAISE ISSUE IF SOMETHING NOT WORKING ;)__

## Points to Note

There is no upload feature yet, files should be manually pre-uploaded.


