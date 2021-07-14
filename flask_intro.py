from flask import Flask, request

app = Flask("Job Site")

items = ["python", "perl", "ruby"]

@app.route("/") #decorator
def hello():
    return f"List of items: {', '.join(items)}"

@app.route("/add")
def add_item():
    item = request.args.get("item")
    items.append(item)
    #http://127.0.0.1:5000/add?item=PHP  so we can add items using the address bar in this way
    return f"No of items is now {len(items)}"


# "export FLASK_APP=flask_intro"     in terminal
# "flask run" to run the app  then follow the link in terminal to see the app
# "flask run --reload" can be used to run the app such that all save changes are reflected immediately