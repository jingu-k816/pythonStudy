from wework_remote import extract_wwr_jobs
from indeed import extract_indeed_jobs
from file import save_to_file

# keyword = input("What do you want to search for?")



# save_to_file(keyword, jobs)

from flask import Flask, render_template, request

app = Flask("JobScrapper", template_folder="web_scrape/templates")

@app.route("/")
def home():
    return render_template("home.html", name="Jingu")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    wwJobs = extract_wwr_jobs(keyword)
    indeedJobs = extract_indeed_jobs(keyword)

    jobs = indeedJobs + wwJobs

    return render_template("search.html", keyword=keyword)

app.run()