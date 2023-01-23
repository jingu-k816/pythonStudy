from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

browser = webdriver.Chrome(options=options)

base_url = "https://ca.indeed.com/jobs?q="
search_term = "junior+developer"

response = browser.get(f"{base_url}{search_term}")
response = browser.page_source

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")

jobs = job_list.find_all("li", recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")

    if zone == None:
        print("job li")
    else:
        print("mosaic li")
