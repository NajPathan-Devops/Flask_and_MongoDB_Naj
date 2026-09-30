
# Flask + MongoDB Student Registration Application

A Python Flask web application integrated with MongoDB Atlas for storing student registration data. The project includes a web-based registration form, REST API endpoints, MongoDB database operations, and environment-based configuration for secure database credentials.

## 🚀 Project Overview

This project was built to practice backend development using:

* Python
* Flask
* MongoDB Atlas
* PyMongo
* REST APIs
* HTML/CSS
* Environment variables

The application allows users to submit student information through a web form and stores the submitted data in MongoDB.

## 🏗️ Architecture

```text
User
 │
 ▼
HTML Registration Form
 │
 ▼
Flask Application
 │
 ├── REST API
 │
 ├── Student Registration
 │
 └── To-Do API
 │
 ▼
PyMongo
 │
 ▼
MongoDB Atlas
 └── flask_assignment
      └── students
```

## 🛠️ Tech Stack

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Backend programming       |
| Flask         | Web framework             |
| MongoDB Atlas | Cloud database            |
| PyMongo       | MongoDB integration       |
| HTML/CSS      | Frontend                  |
| python-dotenv | Environment configuration |
| REST API      | Backend API communication |

## 📁 Project Structure

```text
Flask_and_MongoDB_Naj/
│
├── templates/
│   ├── form.html
│   └── success.html
│
├── app.py
├── backend_data.json
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Application Features

### 1. Student Registration

The application provides a registration form where users can submit student information.

Submitted data is stored in the MongoDB `students` collection.

### 2. MongoDB Atlas Integration

The Flask application connects to MongoDB Atlas using PyMongo.

Database:

```text
flask_assignment
```

Collection:

```text
students
```

The MongoDB connection string is loaded from an environment variable rather than being stored directly in the source code.

### 3. REST API

The project includes API endpoints for interacting with the backend.

Example:

```text
GET /
GET /api
POST /submit
```

### 4. To-Do API

The project also contains a small To-Do functionality demonstrating another MongoDB operation.

## 🔐 Environment Configuration

Create a `.env` file in the project root:

```env
MONGO_URI=your_mongodb_atlas_connection_string
```

The `.env` file is intentionally excluded from Git using `.gitignore`.

**Never commit your MongoDB username, password, or connection string to GitHub.**

## 💻 Local Setup

### 1. Clone the repository

```bash
git clone git@github.com:NajPathan-Devops/Flask_and_MongoDB_Naj.git
cd Flask_and_MongoDB_Naj
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

Linux / WSL:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MongoDB

Create `.env` and add your MongoDB Atlas connection string:

```env
MONGO_URI=your_mongodb_atlas_connection_string
```

### 6. Run the application

```bash
python app.py
```

The application runs locally on:

```text
http://127.0.0.1:5000
```

## 🧪 Testing

After starting the Flask server, verify the application in a browser:

```text
http://127.0.0.1:5000/
```

Test the API endpoint:

```text
http://127.0.0.1:5000/api
```

Submit a student through the registration form and verify that the data is stored in the MongoDB Atlas `students` collection.

## 🔄 Application Flow

```text
1. User opens the Flask application
              ↓
2. User fills the student registration form
              ↓
3. Flask receives POST /submit
              ↓
4. PyMongo connects to MongoDB Atlas
              ↓
5. Student data is inserted
              ↓
6. Success page is displayed
```

## 🔒 Security Practices

* MongoDB credentials are stored using environment variables.
* `.env` is excluded using `.gitignore`.
* Python virtual environment is excluded from Git.
* Sensitive database credentials should never be committed to the repository.

## 📚 What I Learned

Through this project, I practiced:

* Building a Flask web application
* Creating Flask routes
* Handling GET and POST requests
* Connecting Python applications to MongoDB Atlas
* Performing MongoDB insert operations with PyMongo
* Creating REST API endpoints
* Using environment variables for configuration
* Managing Python virtual environments
* Protecting sensitive configuration files with `.gitignore`
* Structuring a small backend application for GitHub

## 🎯 Project Outcome

A working Flask backend was developed with MongoDB Atlas integration and a browser-based student registration interface.

The project demonstrates practical experience with **Python backend development, Flask, MongoDB, REST APIs, and secure environment-based configuration**.

## 👩‍💻 Author

**Naj Pathan**

GitHub: `NajPathan-Devops`

---

⭐ This project was created as part of my backend and DevOps learning journey.

