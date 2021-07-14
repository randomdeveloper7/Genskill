
import requests
import bs4
import psycopg2

import sys

def fetch_jobs():
    url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="
    headers={"appid" : "109",
             "systemid" : "109"}  #appid and systemid can be found from inspect element of the site.  In the inspect element pane go to networks section and then click on the url and check the request-headers section in the right pane of the inspect element.
    r = requests.get(url, headers = headers)
    data = r.json()  #data is a dict object with keys : ['noOfJobs', 'clusters', 'jobDetails', 'fatFooter', 'suggesterModel', 'seo', 'bellyFilters', 'sid', 'isLoggedIn', 'variantName']
    return data['jobDetails']


def insert_to_file():
    url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="
    headers={"appid" : "109",
             "systemid" : "109"}  #appid and systemid can be found from inspect element of the site.  In the inspect element pane go to networks section and then click on the url and check the request-headers section in the right pane of the inspect element.
    r = requests.get(url, headers = headers)
    f = open("naukri-data.txt", 'w')
    data = r.json()  # data is a dict object
    for i in data["jobDetails"]:  # i is a dict object
        for key, value in i.items():
            f.write(f"{key}          :::::::          {value}\n")
        f.write("\n\n")
    f.close()


def insert_jobs(jobs):
    conn = psycopg2.connect("dbname = naukri user = hmj")
    cur = conn.cursor()
    for i in jobs:
        title = i['title']
        jobId = i['jobId']
        company_name = i['companyName']
        jd_url = i['jdURL']
        jd = i['jobDescription']
        soup = bs4.BeautifulSoup(i['jobDescription'], features= "html.parser")
        jd = str(soup.text)
        cur.execute("""insert into openings (title, jobId, company_name, jd_text, jd_url) 
                        values (%s, %s, %s, %s, %s) """, (title, jobId, company_name, jd, jd_url))
    conn.commit()

def create_db():
        conn = psycopg2.connect("dbname = naukri user = hmj")
        cur = conn.cursor()
        f = open("jobs.sql")
        sql_code = f.read()
        f.close()
        cur.execute(sql_code)
        conn.commit()


def main(arg):
    if arg == "create":
        create_db()
    elif arg == "crawl":
        jobs = fetch_jobs();
        insert_jobs(jobs)
    else:
        print(f"Unknown command {arg}")

if (__name__ == "__main__"):  #if the python module is run directly instead of importing then this section will be exectued
    main(sys.argv[1])
             
#dict_keys(['title', 'logoPath', 'logoPathV3', 'jobId', 'jobType', 'currency', 'footerPlaceholderLabel', 
#'footerPlaceholderColor', 'companyName', 'isSaved', 'tagsAndSkills', 'placeholders', 'companyId', 'jdURL', 'staticUrl', 'ambitionBoxData', 'jobDescription', 
#'showMultipleApply', 'groupId', 'isTopGroup', 'createdDate'])  -> these are the keys present for every 'job' in the data 

