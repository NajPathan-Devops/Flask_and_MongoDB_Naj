from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
db = client["flask_assignment"]
collection = db["students"]
todo_collection = db["todo_items"]


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


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    todo_item = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    todo_collection.insert_one(todo_item)

    return jsonify({
        "message": "To-Do item submitted successfully"
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
