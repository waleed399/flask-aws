# app.py
import os

from flask import Flask, render_template, request
import re
import boto3
from flask_pymongo import PyMongo
from pymongo import MongoClient

s3 = boto3.client('s3')
client = MongoClient("mongo:27017")
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

db = client.project_db
users_collection = db.users

def is_valid_email(email):
    # Regular expression pattern for valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        if is_valid_email(email):
            user_data = {"name": name, "email": email}
            users_collection.insert_one(user_data)
            image_uri = "https://flask-aws-bucket.s3.eu-central-1.amazonaws.com/surf.jpg"
            return render_template("hello.html", name=name, image_url=image_uri)
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5555)
