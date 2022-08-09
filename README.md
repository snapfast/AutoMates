# AutoMates
Automate the finding people/jobs on Apps like LinkedIn, Bumble, AngelList.


## Setup 

Run the command to install the only package needed `selenium`.  
*Optional: Create separate python environment.*

1. `pip3 install selenium`
2. `python first_setup.py`
3. Run anything from below.

### Linkedin
```python
python3 recommended_jobs.py  # to apply for recommended jobs in Jobs Section
python3 search_jobs.py "software engineer" gurgaon  # to search for jobs per location
```

### Bumble
```python
python3 run.py # just right swipe only, it does a right swipe on random time, 3 secs to 13 secs.
```

### Angel List
TBD


__NOTE: RAISE ISSUE IF SOMETHING NOT WORKING ;)__

### Uploads

There is no limit to the number of files you can list in the uploads section. 
The program takes the titles from the input boxes and tries to match them with 
list in the config file.


