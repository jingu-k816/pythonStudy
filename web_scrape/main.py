from wework_remote import extract_wwr_jobs
from indeed import extract_indeed_jobs

keyword = input("What do you want to search for?")

wwJobs = extract_wwr_jobs(keyword)
indeedJobs = extract_indeed_jobs(keyword)

jobs = indeedJobs + wwJobs

file = open(f"{keyword}_jobs.csv", "w")

file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
