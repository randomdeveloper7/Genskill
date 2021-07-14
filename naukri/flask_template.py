"""
We can write html, CSS code etc in seperate files and use it in our python module using render_template.
For doing this we have to make a new directory called templates in the directory where our python file is present
and add the html files we want to use to this directory """


from flask import Flask, request, render_template
import psycopg2

app = Flask("Naukri")

@app.route("/")
def index():
    conn = psycopg2.connect("dbname = naukri user  = hmj")
    cur = conn.cursor()
    cur.execute("select count(*) from openings")
    njobs = cur.fetchall()[0][0]      #cur.fetchall() returns the result of the query as a list of tuples, where each tuple corresponds to seperate rows
    return render_template("main.html", njobs = njobs)


@app.route("/jobs")
def jobs():
    conn = psycopg2.connect("dbname = naukri user  = hmj")
    cur = conn.cursor()

    cur.execute("select title, company_name, jd_text from openings")

    return render_template("jobslist.html", jobs = cur.fetchall())

if(__name__ == "__main__"):
    app.run() 
    """
    instead of using export FLASK_APP=filename and then flask run we can directly run it by running the python file now.
    """