"""
instantiate new object app which controls everything in flask
 __name__ indicates identity of file
run app if identity is main
"""

from flask import Flask, render_template, request
import requests
from flask_pymongo import MongoClient 

app = Flask(__name__)
app.config['DEBUG'] = True

connection = MongoClient()
db = connection.project #database name
collection = connection.signup #collection name

@app.route('/')
def hello():
    return render_template('hello.html')

#page2
@app.route('/page2')
def banana():
    return render_template("page2.html")

@app.route('/page2', methods = ["GET", "POST"])
def banana_form():
    if request.method == "POST":
        number = request.form["quan"]
        collection.insert_one({"quan": number})
    else:
        return render_template("page2.html")

@app.errorhandler(404)
def not_found(error):
    return "Sorry, page not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')
