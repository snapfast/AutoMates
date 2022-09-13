import first_setup
from BUMBLE import swipe
from LINKEDIN import recommended_jobs as l_rec
from LINKEDIN import search_jobs
from NAUKRI import recommended_jobs as n_rec

# first time setup
# ask the operating system

print("First Setup ?\n 1. Yes\n 2. No")
FIRST_SETUP = int(input())
if FIRST_SETUP == 1:
	first_setup.setupCD('linux')


# ask the Service to automate

print("""
Which service to automate ?
1. Angel List
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
	""")
	LINKEDIN_SERVICE = int(input())
	if LINKEDIN_SERVICE == 1:
		print("Applying Linkedin Recommended..")
		lb = l_rec.LinkedinBot()
		lb.click_job()
	elif LINKEDIN_SERVICE == 2:
		print("Searching on Linkedin.")
		position = input("Search by post name")
		location = input("Enter job location")
		l = search_jobs.LinkedinBot()
		l.do_search(position, location)
		l.click_easy_jobs()
elif SERVICE == 3:
	print("Naukri Selected")
	print("""
	Applying Naukri Recommended Jobs.
	""")
	n = n_rec.NaukriBot()
	n.click_job()
elif SERVICE == 4:
	print("Bumble Selected")
	print("Swiping right on all profiles :)")
	b = swipe.BumbleBot()
	b.right_swipe()
else:
	exit()



# if error, ask for going back to previous menu.

