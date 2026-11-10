#  TalentHub – Campus Placement Management System

TalentHub is a full-stack web application designed to simplify and automate the college placement process. It provides a centralized platform where students can explore job opportunities, apply for eligible positions, companies can manage recruitment activities, and placement coordinators can monitor overall placement progress.

The system streamlines the complete placement workflow, from student registration and job applications to shortlisting, interview scheduling, offer management, and placement statistics.

##  Key Features

### Student Module
- Student registration and secure login.
- View available job opportunities.
- Check eligibility based on CGPA, branch, and active backlogs.
- Apply for eligible job openings.
- Track application status.
- View interview schedules.
- Accept or decline placement offers.

### Company Module
- Company/HR login.
- Create and manage job listings.
- Define eligibility criteria for job openings.
- View student applications.
- Shortlist or reject applicants.
- Schedule interviews.
- Update interview results.
- Issue placement offers with package details.

###  Placement Coordinator Module
- Coordinator authentication.
- Manage and monitor placement activities.
- View student and company details.
- Track applications across companies.
- Monitor offers issued and accepted.
- View overall placement statistics.
- Generate an overview of placement performance.

##  Technologies Used

| Component | Technology |
|---|---|
| Frontend | React.js |
| Backend | Python, FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Authentication | JWT |
| API Communication | REST API |
| Frontend Styling | CSS |
| API Testing | Swagger UI |
| Version Control | Git & GitHub |

##  Project Structure

```text
TalentHub/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── services/
│   │   └── schemas/
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── talenthub.db
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── api.js
│   │
│   └── package.json
│
└── README.md
```

##  How to Run the Project Locally

### 1. Prerequisites

Install the following before running the project:

- Python 3.9 or above
- Node.js and npm
- Visual Studio Code (recommended)
- Git

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd TalentHub
```

### 3. Start the Backend

Open the terminal and navigate to the backend folder.

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```

Backend URL:

http://127.0.0.1:8000

Swagger API Documentation:

http://127.0.0.1:8000/docs

### 4. Start the Frontend

Open another terminal and navigate to the frontend folder.

```bash
cd frontend
```

Install the required packages:

```bash
npm install
```

Start the frontend development server:

```bash
npm run dev
```

Open the frontend in your browser using the URL displayed in the terminal (usually):

http://localhost:5173

## 🔄 Application Workflow

1. **Student Registration/Login:** Students securely log in to the portal.
2. **Job Listings:** Students explore available placement opportunities.
3. **Eligibility Verification:** The system checks student eligibility based on company requirements.
4. **Job Application:** Eligible students apply for job openings.
5. **Shortlisting:** Companies review applications and shortlist suitable candidates.
6. **Interview Scheduling:** Companies schedule interviews for shortlisted students.
7. **Interview Results:** Companies update interview results.
8. **Offer Management:** Successful candidates receive placement offers.
9. **Offer Acceptance:** Students accept or decline the offers.
10. **Placement Monitoring:** Coordinators monitor placement activities and statistics.

##  Security Features
- JWT-based authentication.
- Role-based access control.
- Password hashing.
- Protected API endpoints.
- Eligibility validation.
- Secure handling of student and company information.

##  Benefits of the System

- Reduces manual placement coordination.
- Simplifies student application tracking.
- Improves communication between students and companies.
- Automates eligibility verification.
- Provides centralized placement information.
- Helps coordinators monitor placement performance.

##  Future Enhancements

- Email notifications for interview schedules.
- Resume upload and management.
- Automated placement reports.
- Advanced analytics and visual dashboards.
- Integration with external job platforms.

##  Project Information

**Project Name:** TalentHub – Campus Placement Management System

**Project Type:** Full-Stack Web Application

**Domain:** Campus Recruitment and Placement Management

**Purpose:** To digitize and streamline the college placement process.

##  Conclusion

TalentHub provides a centralized and efficient platform for managing campus recruitment activities. By connecting students, companies, and placement coordinators, the system simplifies the placement process, improves transparency, and makes recruitment management more organized.

---
## AUTHOR
Anushree Angadi
