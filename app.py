# app.py
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
import os

from flask import Flask, render_template, request
import re
import boto3
from flask_pymongo import PyMongo

s3 = boto3.client('s3')

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

# Accessing the MongoDB collection
collection = mongo.db.users


def generate_presigned_url(bucket_name, key):
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': key},
        ExpiresIn=3600
    )
    return url


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
            collection.insert_one(user_data)
            # Generate the pre-signed URL for the image
            bucket_name = 'flask-aws-bucket'
            object_name = 'surf.jpg'
            image_uri = generate_presigned_url(bucket_name, object_name)
            return render_template("hello.html", name=name, image_url=image_uri)
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5555)
