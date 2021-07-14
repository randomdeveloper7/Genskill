#returning raw html directly 



from flask import Flask, request
import psycopg2

app = Flask("Naukri")

@app.route("/")
def index():
    conn = psycopg2.connect("dbname = naukri user  = hmj")
    cur = conn.cursor()
    cur.execute("select count(*) from openings")
    njobs = cur.fetchall()[0][0]      #cur.fetchall() returns the result of the query as a list of tuples, where each tuple corresponds to seperate rows
    return f"""
    <html>
    <head>
        <title> Jobs Page </title>
    </head>

    <body>
        <h1> Welcome to the jobs page </h1>
        There are currently <a href = "/jobs">{njobs}</a> jobs
    </body>
    </html>
    """


@app.route("/jobs")
def jobs():
    conn = psycopg2.connect("dbname = naukri user  = hmj")
    cur = conn.cursor()

    ret = []
    cur.execute("select title, company_name, jd_text from openings;")
    for title, company_name, jd in cur.fetchall():
        item = f"<b>{title}</b> : {company_name} <br/> {jd}"
        ret.append(item)

    return f"List of items: {'<hr/>'.join(ret)}"