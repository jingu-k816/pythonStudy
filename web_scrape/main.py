from wework_remote import extract_wwr_jobs
from indeed import extract_indeed_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

wwJobs = extract_wwr_jobs(keyword)
indeedJobs = extract_indeed_jobs(keyword)

jobs = indeedJobs + wwJobs

save_to_file(keyword, jobs)
