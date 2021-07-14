from flask import Flask, request
import psycopg2

app = Flask("Job SIte")

@app.route("/") #decorator
def hello():
    conn = psycopg2.connect("dbname = naukri user  = hmj")
    cur = conn.cursor()

    ret = []
    cur.execute("select title, company_name, jd_text from openings;")
    for title, company_name, jd in cur.fetchall():
        item = f"<b>{title}</b> : {company_name} <br/> {jd}"
        ret.append(item)

    return f"List of items: {'<hr/>'.join(ret)}"