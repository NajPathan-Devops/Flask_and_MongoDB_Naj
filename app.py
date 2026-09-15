from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGO_URI"))
db = client["flask_assignment"]
collection = db["students"]


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/api")
def api():
    with open("backend_data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")

        student = {
            "name": name,
            "email": email,
            "course": course
        }

        collection.insert_one(student)

        return render_template("success.html")

    except Exception as e:
        return render_template("form.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
