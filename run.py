import setup
from time import sleep
from BUMBLE import swipe
from LINKEDIN import recommended_page
from LINKEDIN import search_jobs
from LINKEDIN import connect_people
from LINKEDIN import profile_stalker
from NAUKRI import recommended_jobs as n_rec

# first time setup
# creating a UI in python using pyqt6
# https://www.youtube.com/watch?v=Vde5SH8e1OQ&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj

print("1. Let me login to the website.\n2. I am already logged in previously using this script.")
FIRST_SETUP = int(input())
if FIRST_SETUP == 1:
	# letting the user to login
	print("Chrome window will open to let you login to the accounts. \nYou have two minutes to login to your account :)")
	sleep(10)
	setup.loginWindow()
else:
	print("skipping setup...")

# ask the Service to automate

print("""
Which service to automate ?
1. WellFound
2. Linkedin
3. Naukri
4. Bumble
0. Exit
	""")
SERVICE = int(input())

# ask input if required
if SERVICE == 1:
	print("No Service found! Ask the dev.")
elif SERVICE == 2:
	print("Linkedin Selected")
	print("""
Choose below ?
1. Apply Linkedin Recommended Jobs.
2. Search based on Position and Location.
3. Connect to Company People (paypal, nvidia, tesla, etc.)
4. Stalk Profiles (opens a link from profile you give, then keeps on.)
	""")
	LINKEDIN_SERVICE = int(input())
	if LINKEDIN_SERVICE == 1:
		print("Applying Linkedin Recommended Page..")
		rp = recommended_page.LinkedinBot()
		rp.click_easy_jobs()
	elif LINKEDIN_SERVICE == 2:
		print("Searching on Linkedin.")
		position = input("\nEnter post name\n")
		location = input("\nEnter job location\n")
		l = search_jobs.LinkedinBot()
		l.do_search(position, location)
		l.click_easy_jobs()
	elif LINKEDIN_SERVICE == 3:
		print("Connecting People on Linkedin.")
		co_name = input("\n Enter the company name in lowercase.\n")
		cp = connect_people.LinkedinBot(co_name)
		cp.connect()
	elif LINKEDIN_SERVICE == 4:
		print("Stalking People on Linkedin.")
		start_profile = input("\n Enter the Profile to start from.\n")
		ps = profile_stalker.LinkedinBot(start_profile)
		ps.stalk_on()
elif SERVICE == 3:
	print("Naukri Selected")
	print("Applying Naukri Recommended Jobs.")
	n = n_rec.NaukriBot()
	n.click_job()
elif SERVICE == 4:
	print("Bumble Selected")
	print("Swiping right on all profiles :P")
	b = swipe.BumbleBot()
	b.right_swipe()
else:
	exit()



# if error, ask for going back to previous menu.

