
# Flask and MongoDB Assignment

## Student Information

**Name:** Naj Pathan  
**Course:** DevOps / Flask and MongoDB Assignment  
**Platform:** Tutedude  

---

## Project Overview

This project is a Flask web application developed as part of the Tutedude Flask and MongoDB assignment.

The application demonstrates a JSON API, a frontend student registration form, and MongoDB Atlas database integration.

The project includes:

- Flask web application
- JSON API route
- HTML frontend form
- MongoDB Atlas integration
- Student data insertion
- Success page
- Error handling
- Environment variables
- Git and GitHub version control

---

## Objective

The objective of this project is to build a Flask application that provides:

1. A JSON API route that reads data from a backend JSON file.
2. A frontend form that accepts student information.
3. MongoDB Atlas integration for storing submitted data.
4. Proper success and error handling.

---

# Task 1 - JSON API Route

A Flask `/api` route was created to read data from the `backend_data.json` file and return the data as JSON.

### API Endpoint

```text
/api
````

### Backend Data File

```text
backend_data.json
```

### Example Data

```json
[
    {
        "id": 1,
        "name": "Naj",
        "course": "DevOps",
        "status": "Learning"
    },
    {
        "id": 2,
        "name": "Student",
        "course": "Flask",
        "status": "Completed"
    }
]
```

### Example API Response

When `/api` is opened in the browser, the application returns the data in JSON format.

```json
[
    {
        "id": 1,
        "name": "Naj",
        "course": "DevOps",
        "status": "Learning"
    },
    {
        "id": 2,
        "name": "Student",
        "course": "Flask",
        "status": "Completed"
    }
]
```

---

# Task 2 - Frontend Form with MongoDB Atlas

A frontend student registration form was created using HTML.

The form contains three fields:

* Name
* Email
* Course

The form sends the submitted data to the Flask backend using a POST request.

### Form Route

```text
/
```

### Form Submission Route

```text
/submit
```

### HTTP Method

```text
POST
```

---

# MongoDB Atlas Integration

MongoDB Atlas is used as the cloud database for storing student information.

The Flask application connects to MongoDB Atlas using the PyMongo library.

### Database

```text
flask_assignment
```

### Collection

```text
students
```

The submitted form data is stored as a MongoDB document.

### Example Document

```json
{
    "name": "Student Name",
    "email": "student@example.com",
    "course": "DevOps"
}
```

MongoDB automatically creates an `_id` for each document.

---

# Success Handling

After the form data is successfully inserted into MongoDB Atlas, the application displays a separate success page.

The success page displays:

```text
Data submitted successfully
```

The page also contains an option to return to the registration form.

---

# Error Handling

If an error occurs while saving the submitted data to MongoDB Atlas, the application does not redirect to the success page.

Instead, an error message is displayed on the same registration form page:

```text
Error saving data. Please try again.
```

This provides basic error handling for database submission failures.

---

# Project Structure

```text
Flask_and_MongoDB_Naj/
│
├── app.py
├── backend_data.json
├── requirements.txt
├── .gitignore
├── README.md
│
└── templates/
    ├── form.html
    └── success.html
```

### File Description

| File                     | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| `app.py`                 | Main Flask application                                       |
| `backend_data.json`      | JSON data used by the API                                    |
| `requirements.txt`       | Python dependencies                                          |
| `.gitignore`             | Prevents sensitive and unnecessary files from being uploaded |
| `README.md`              | Project documentation                                        |
| `templates/form.html`    | Student registration form                                    |
| `templates/success.html` | Success page                                                 |

---

# Technologies Used

* Python 3
* Flask
* PyMongo
* MongoDB Atlas
* HTML
* JSON
* python-dotenv
* Git
* GitHub
* WSL / Ubuntu

---

# Flask Routes

| Route     | Method | Description                                |
| --------- | ------ | ------------------------------------------ |
| `/`       | GET    | Displays the student registration form     |
| `/api`    | GET    | Returns JSON data from `backend_data.json` |
| `/submit` | POST   | Stores form data in MongoDB Atlas          |

---

# Environment Variables

The MongoDB Atlas connection string is stored using an environment variable.

A `.env` file is created locally in the project directory.

Example:

```text
MONGO_URI=your_mongodb_atlas_connection_string
```

The actual MongoDB connection string should be used locally.

The `.env` file is not uploaded to GitHub because it contains sensitive database credentials.

---

# Security

Sensitive information such as MongoDB passwords and connection strings should never be uploaded to GitHub.

The following files and folders are excluded using `.gitignore`:

```text
venv/
.env
__pycache__/
*.pyc
```

The `.env` file is intentionally excluded from the repository.

---

# Installation and Setup

## Step 1 - Clone the Repository

```bash
git clone https://github.com/NajPathan-Devops/Flask_and_MongoDB_Naj.git
```

Go into the project directory:

```bash
cd Flask_and_MongoDB_Naj
```

---

## Step 2 - Create Virtual Environment

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate it on Linux / WSL:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

---

## Step 3 - Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Step 4 - Configure MongoDB Atlas

Create a `.env` file in the project root directory.

Add:

```text
MONGO_URI=your_mongodb_atlas_connection_string
```

Replace the example value with your own MongoDB Atlas connection string.

Do not share the actual password publicly.

---

## Step 5 - Run the Application

Run the Flask application:

```bash
python app.py
```

The application will start at:

```text
http://127.0.0.1:5000/
```

---

# Testing

## Test 1 - Home Page

Open:

```text
http://127.0.0.1:5000/
```

The Student Registration Form should appear.

---

## Test 2 - JSON API

Open:

```text
http://127.0.0.1:5000/api
```

The JSON data from `backend_data.json` should be displayed.

---

## Test 3 - Submit Student Data

Open:

```text
http://127.0.0.1:5000/
```

Enter the required information:

```text
Name
Email
Course
```

Click the **Submit** button.

The Flask application receives the form data and attempts to store it in MongoDB Atlas.

---

## Test 4 - Successful Submission

When the data is successfully stored in MongoDB Atlas, the application displays:

```text
Data submitted successfully
```

The submitted data can then be checked in the MongoDB Atlas collection:

```text
flask_assignment
└── students
```

---

## Test 5 - Error Handling

If an error occurs while saving the data, the application displays:

```text
Error saving data. Please try again.
```

on the same registration form page.

---

# MongoDB Atlas Verification

The submitted student information can be verified inside MongoDB Atlas.

### Database

```text
flask_assignment
```

### Collection

```text
students
```

### Example Stored Document

```text
name: Student Name
email: student@example.com
course: DevOps
```

---

# Git and GitHub

Git was used to manage the project and GitHub was used to store the source code.

The repository was initialized using:

```bash
git init
```

The main branch was created using:

```bash
git branch -M main
```

Files were added using:

```bash
git add .
```

The project was committed using:

```bash
git commit -m "Complete Flask and MongoDB assignment"
```

The project was then pushed to GitHub.

---

# GitHub Repository

The complete project source code is available here:

[https://github.com/NajPathan-Devops/Flask_and_MongoDB_Naj](https://github.com/NajPathan-Devops/Flask_and_MongoDB_Naj)

---

# Screenshots / Evidence

The project documentation contains screenshots showing the implementation and testing process.

The screenshots include:

1. Flask application running
2. JSON API response
3. Student registration form
4. MongoDB Atlas project
5. MongoDB Atlas connection
6. Data stored in MongoDB Atlas
7. GitHub repository

---

# Learning Outcomes

Through this assignment, I learned and practiced:

* Creating a Flask application
* Creating Flask routes
* Creating a JSON API
* Reading data from a JSON file
* Returning JSON responses
* Creating HTML forms
* Handling POST requests
* Receiving form data in Flask
* Connecting Flask with MongoDB Atlas
* Using PyMongo
* Inserting documents into MongoDB
* Handling database errors
* Using environment variables
* Protecting sensitive database credentials
* Using Git
* Creating and managing a GitHub repository

---

# Conclusion

This project demonstrates a Flask application with both API and frontend functionality.

The `/api` route reads data from a JSON file and returns it as JSON.

The frontend registration form collects student information and sends it to the Flask backend.

The Flask backend stores the submitted information in MongoDB Atlas.

The application also provides separate success handling and error handling for form submissions.

Git and GitHub were used for version control and source code management.

---

# Author

**Naj Pathan**

GitHub:

[https://github.com/NajPathan-Devops](https://github.com/NajPathan-Devops)

---


