from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_page_count(keyword):
    options = Options()
    browser = webdriver.Chrome(options=options)

    base_url = "https://ca.indeed.com/jobs?q="
    response = browser.get(f"{base_url}{keyword}")
    response = browser.page_source

    soup = BeautifulSoup(response, "html.parser")

    pagination = soup.find("nav", {"aria-label": "pagination"})
    if pagination == None:
        print("inside pagination none")
        return 1
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

def extract_indeed_jobs(keyword):
    options = Options()

    browser = webdriver.Chrome(options=options)

    pages = get_page_count(keyword)
    for page in range(pages):
        base_url = "https://ca.indeed.com/jobs"

        response = browser.get(f"{base_url}?q={keyword}&start={page*10}")
        response = browser.page_source

        results = []
        soup = BeautifulSoup(response, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")

        jobs = job_list.find_all("li", recursive=False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")

            if zone == None:
                anchor = job.select_one("h2 a")
                title = job.find("h2", class_="jobTitle")
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")

                job_data = {
                    'link': f"https://ca.indeed.com{link}",
                    'company': company.string,
                    'location': location.string,
                    'position': title.string
                }
                results.append(job_data)

        for result in results:
            print(result)
            print("/////////////////////////////////////////////////////////////")

extract_indeed_jobs("junior+developer")