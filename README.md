.

# AWS_Naj — AWS Cloud Deployment Project

## 🚀 Project Overview

A full-stack web application built with **Python Flask** and **Node.js/Express.js**, containerized with Docker and deployed using multiple AWS services and deployment approaches.

This project demonstrates practical experience with:

**Docker → Amazon ECR → Amazon ECS/Fargate → AWS VPC & Security Groups**

It also includes EC2-based deployment and cloud networking configuration.

---

## 🏗️ Architecture

```text
                    AWS Cloud
                       │
          ┌────────────┴────────────┐
          │                         │
       Amazon EC2              Amazon ECS
          │                     / Fargate
          │                         │
       Docker                  Docker Images
          │                         │
          │                    Amazon ECR
          │                         │
          └────────────┬────────────┘
                       │
                  VPC / Network
                       │
                Security Groups
                       │
              Full-Stack Application
                ┌──────────────┐
                │   Frontend   │
                │ Express.js   │
                │    :3000     │
                └──────┬───────┘
                       │
                ┌──────▼───────┐
                │   Backend    │
                │    Flask     │
                │    :5000     │
                └──────────────┘
```

---

## ☁️ AWS Services Used

| AWS Service         | Purpose                        |
| ------------------- | ------------------------------ |
| **Amazon EC2**      | Virtual server deployment      |
| **Amazon ECR**      | Docker image storage           |
| **Amazon ECS**      | Container orchestration        |
| **AWS Fargate**     | Serverless container execution |
| **Amazon VPC**      | Network isolation              |
| **Security Groups** | Network traffic control        |

---

## 🛠️ Technology Stack

### Frontend

* Node.js
* Express.js
* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### DevOps / Cloud

* Docker
* Docker Compose
* Amazon EC2
* Amazon ECR
* Amazon ECS
* AWS Fargate
* Amazon VPC
* Security Groups
* Linux
* Git & GitHub

---

## 📁 Project Structure

```text
AWS_Naj/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── server.js
│   ├── package.json
│   ├── package-lock.json
│   └── Dockerfile
│
├── screenshots/
│   ├── ...
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# 🐳 Docker Deployment

The application was first containerized using Docker.

Two separate Docker images were created:

```text
Backend → Flask
Frontend → Node.js / Express
```

### Backend Docker Image

```text
najpathan/docker-backend:latest
```

### Frontend Docker Image

```text
najpathan/docker-frontend:latest
```

---

## ▶️ Run with Docker Compose

Start the complete application:

```bash
docker compose up --build
```

The services run on:

```text
Frontend → Port 3000
Backend  → Port 5000
```

Stop the application:

```bash
docker compose down
```

---

# 💻 Amazon EC2 Deployment

The application was also deployed using **Amazon EC2**.

Two deployment approaches were tested:

### 1. Single EC2 Deployment

Frontend and backend containers were deployed on an EC2 instance.

```text
EC2
 ├── Frontend Container → :3000
 └── Backend Container  → :5000
```

### 2. Separate EC2 Deployment

Frontend and backend were deployed separately using EC2 instances.

```text
EC2 Instance 1
 └── Frontend → :3000

EC2 Instance 2
 └── Backend → :5000
```

Temporary public IPs were used during testing and are no longer active.

---

# 📦 Amazon ECR

Docker images were pushed to **Amazon Elastic Container Registry (ECR)**.

Repositories created for the project:

```text
aws-naj-backend
aws-naj-frontend
```

Typical workflow:

```text
Build Docker Image
        ↓
Tag Image
        ↓
Authenticate with Amazon ECR
        ↓
Push Image to ECR
        ↓
Use Image in ECS
```

Example:

```bash
docker build -t aws-naj-backend ./backend
docker build -t aws-naj-frontend ./frontend
```

After tagging the images with the ECR repository URI, they were pushed to Amazon ECR.

---

# 🚀 Amazon ECS / Fargate Deployment

The Docker images stored in Amazon ECR were used for container deployment with **Amazon ECS**.

### ECS Configuration

```text
Cluster:
AWS-Naj-ECS-Cluster

Service:
AWS-Naj-Service

Launch Type:
Fargate

Platform:
Linux / x86_64
```

The ECS task was configured to run the frontend and backend containers.

```text
ECS Task
│
├── Frontend Container
│   └── Port 3000
│
└── Backend Container
    └── Port 5000
```

For the ECS deployment, the frontend communicates with the backend using the configured container networking.

---

# 🌐 VPC & Security Groups

The application was deployed within an AWS VPC environment.

Security groups were configured to control inbound traffic.

Example application port:

```text
TCP 3000 → Frontend
```

Additional backend/network rules were configured as required for communication between the application components.

> Public access rules were used temporarily for testing and should be restricted in a production environment.

---

# 🧪 Application Testing

The application was tested after deployment to verify:

* Frontend accessibility
* Backend availability
* Container communication
* Docker image functionality
* EC2 deployment
* ECR image availability
* ECS task execution
* Network configuration
* Security group rules

---

# 📸 Screenshots

The `screenshots/` directory contains project evidence, including:

* Docker builds
* Docker containers
* Docker Compose
* EC2 deployment
* ECR repositories
* Docker image push
* ECS configuration
* Fargate deployment
* VPC configuration
* Security groups
* Application testing

These screenshots provide evidence of the AWS deployment process.

---

# 🧹 AWS Resource Cleanup

Temporary AWS resources created during testing were cleaned up after completing the deployment experiments.

This included temporary compute, container, and networking resources where applicable.

> Temporary public IPs were used during testing and are no longer active.

---

# 📊 Project Results

Successfully demonstrated a complete cloud deployment workflow:

```text
Application
     ↓
Docker
     ↓
Docker Images
     ↓
Amazon ECR
     ↓
Amazon ECS / Fargate
     ↓
AWS VPC
     ↓
Security Groups
     ↓
Running Application
```

The project provided hands-on experience with containerization, cloud infrastructure, networking, and AWS deployment.

---

# 🎯 Skills Demonstrated

* AWS Cloud
* Amazon EC2
* Amazon ECR
* Amazon ECS
* AWS Fargate
* AWS VPC
* Security Groups
* Docker
* Docker Compose
* Linux
* Node.js
* Express.js
* Python
* Flask
* Containerized application deployment
* Cloud networking
* Git & GitHub
* Troubleshooting and deployment testing

---

# 📚 Key Learning

Through this project, I gained practical experience in:

* Creating and managing AWS EC2 instances
* Deploying applications on cloud infrastructure
* Creating Docker images
* Running multi-container applications with Docker Compose
* Publishing Docker images to Amazon ECR
* Deploying containers using Amazon ECS/Fargate
* Configuring VPC networking
* Managing AWS Security Groups
* Connecting frontend and backend containers
* Testing and troubleshooting cloud deployments
* Cleaning up temporary AWS resources

---

# 🔗 Project

**GitHub Repository:** `NajPathan-Devops/AWS_Naj`

**Docker Images:**

* `najpathan/docker-backend:latest`
* `najpathan/docker-frontend:latest`

---

# 👩‍💻 Author

**Naj Pathan**

Aspiring Cloud / DevOps Engineer

Skills: AWS • Docker • Kubernetes • Terraform • Jenkins • Linux • CI/CD

---

## ⭐ Project Summary

**AWS_Naj** demonstrates a complete practical cloud deployment workflow using **Docker, Amazon EC2, Amazon ECR, Amazon ECS/Fargate, VPC, and Security Groups**.

The project showcases hands-on experience in deploying and managing a containerized full-stack application on AWS.

.


