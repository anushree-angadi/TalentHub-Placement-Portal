# TalentHub Plus – Campus Placement Portal

An improved, separate placement portal starter built with React + Vite, FastAPI and SQLite.

## Features
- Role-based demo login: Student, Company HR, Placement Coordinator
- Student dashboard: jobs, eligibility, application status, profile summary
- Company dashboard: post jobs and review applicants
- Coordinator dashboard: placement metrics and application overview
- Responsive modern UI with sidebar navigation
- SQLite database initialized automatically

## Requirements
- Python 3.10+
- Node.js 18+ and npm

## Run on Windows (PowerShell)

### Backend
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend (open a second terminal)
```powershell
cd frontend
npm install
npm run dev
```
Open the Vite URL shown in the terminal (normally http://localhost:5173).

## Demo accounts
Password for all accounts: `password123`

| Role | Email |
|---|---|
| Student | student@talenthub.edu |
| Company HR | hr@talenthub.edu |
| Coordinator | coordinator@talenthub.edu |

This is a learning/demo application. Change demo credentials, add production-grade authentication,
file validation, authorization checks, HTTPS, backups and deployment configuration before real use.
