from wework_remote import extract_wwr_jobs
from indeed import extract_indeed_jobs
from file import save_to_file

# keyword = input("What do you want to search for?")

# save_to_file(keyword, jobs)

from flask import Flask, render_template, request

app = Flask("JobScrapper", template_folder="web_scrape/templates")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="Jingu")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        wwJobs = extract_wwr_jobs(keyword)
        indeedJobs = extract_indeed_jobs(keyword)

        jobs = indeedJobs + wwJobs
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run()