# app.py
import os

from flask import Flask, render_template, request, redirect
import re
import boto3
from flask_pymongo import PyMongo
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
s3 = boto3.client('s3', region_name=os.getenv("REGION"))

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

# Accessing the MongoDB collection
collection = mongo.db.users


def is_valid_email(email):
    # Regular expression pattern for valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


@app.route('/image')
def image():
    url = s3.generate_presigned_url('get_object', Params={'Bucket': os.getenv("S3_BUCKET_NAME"), 'Key': os.getenv("S3_OBJECT_KEY")})
    return redirect(url)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        if is_valid_email(email):
            user_data = {"name": name, "email": email}
            collection.insert_one(user_data)
            image_url = "/image"
            return render_template("hello.html", name=name, image_url=image_url)
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5555)
