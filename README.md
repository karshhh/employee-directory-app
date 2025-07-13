# 🧑‍💼 Employee Directory - Flask App

This is a simple two-tier Flask application to manage an Employee Directory using SQLite as the backend database. It allows you to add, view, and store employee details such as name, department, and role.

---

## 🛠 Tech Stack

- **Frontend**: HTML (Jinja2 templates)
- **Backend**: Python Flask
- **Database**: SQLite
- **Containerization**: Docker
- **Optional**: Docker Compose, Jenkins, Kubernetes

---

## 📂 Project Structure

employee-directory-app/
├── app.py
├── templates/
│ └── index.html
├── requirements.txt
├── Dockerfile
├── Dockerfile-multistage
├── docker-compose.yml
├── message.sql
├── Jenkinsfile
├── Makefile
├── k8s/
│ └── app.yml
├── eks-manifests/
│ └── app.yml
├── README.md
└── dummy.txt

yaml
---

## ⚙️ Environment Variables

- `EMPLOYEE_DB`: Name of the SQLite database file  
  Default: `employees.db`

You can define it in:
- `.env` file
- Docker `-e` flag
- `docker-compose.yml`

---

## 🚀 How to Run

### ✅ Option 1: Run Locally with Python

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable (optional)
export EMPLOYEE_DB=employees.db

# Run the app
python app.py
Visit http://localhost:5000

🐳 Option 2: Run with Docker
Build the Image
docker build -t employee-app .

Run the Container

docker run -p 5000:5000 -e EMPLOYEE_DB=employees.db employee-app

🐳 Option 3: Run with Docker Compose
docker-compose up --build
🔍 How to Check DB Contents (SQLite)
Step 1: Enter the running container
docker ps
docker exec -it <container_id> bash

Step 2: Install SQLite and inspect DB
apt update && apt install sqlite3 -y
sqlite3 employees.db

Step 3: Query the database
.tables
SELECT * FROM employees;
.exit
