from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import Base, engine, get_db
from models import User, Job, Application

app = FastAPI(title="TalentHub Plus API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)
Base.metadata.create_all(bind=engine)

def seed():
    db = next(get_db())
    if not db.query(User).first():
        db.add_all([
            User(name="Aarav Sharma", email="student@talenthub.edu", password="password123", role="student"),
            User(name="TalentHub Recruiter", email="hr@talenthub.edu", password="password123", role="company"),
            User(name="Placement Coordinator", email="coordinator@talenthub.edu", password="password123", role="coordinator"),
        ])
        db.add_all([
            Job(title="Graduate Software Engineer", company="NovaTech", location="Bengaluru", package=8.5, min_cgpa=7.0, description="Build and maintain modern software products."),
            Job(title="Data Analyst", company="Insight Labs", location="Hyderabad", package=6.0, min_cgpa=6.5, description="Analyze datasets and create business insights."),
            Job(title="AI/ML Intern", company="NeuralWorks", location="Remote", package=5.0, min_cgpa=7.5, description="Work on machine learning prototypes."),
        ])
        db.commit()
    db.close()

seed()

class LoginBody(BaseModel):
    email: str
    password: str

class JobBody(BaseModel):
    title: str
    company: str
    location: str = "India"
    package: float = 0
    min_cgpa: float = 0
    description: str = ""

class ApplyBody(BaseModel):
    student_name: str
    student_email: str
    job_id: int

@app.get("/")
def home():
    return {"message": "Welcome to TalentHub Plus API", "docs": "/docs"}

@app.post("/api/login")
def login(body: LoginBody, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email, User.password == body.password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"id": user.id, "name": user.name, "email": user.email, "role": user.role}

@app.get("/api/jobs")
def jobs(db: Session = Depends(get_db)):
    return db.query(Job).order_by(Job.id.desc()).all()

@app.post("/api/jobs")
def create_job(body: JobBody, db: Session = Depends(get_db)):
    job = Job(**body.model_dump())
    db.add(job); db.commit(); db.refresh(job)
    return job

@app.post("/api/applications")
def apply(body: ApplyBody, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == body.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    existing = db.query(Application).filter(
        Application.student_email == body.student_email,
        Application.job_id == body.job_id
    ).first()
    if existing:
        raise HTTPException(status_code=409, detail="You have already applied")
    application = Application(**body.model_dump())
    db.add(application); db.commit(); db.refresh(application)
    return application

@app.get("/api/applications")
def applications(db: Session = Depends(get_db)):
    return db.query(Application).order_by(Application.id.desc()).all()

@app.patch("/api/applications/{application_id}")
def update_application(application_id: int, status: str, db: Session = Depends(get_db)):
    app_item = db.query(Application).filter(Application.id == application_id).first()
    if not app_item:
        raise HTTPException(status_code=404, detail="Application not found")
    if status not in ["Applied", "Shortlisted", "Interview", "Selected", "Rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    app_item.status = status
    db.commit(); db.refresh(app_item)
    return app_item

@app.get("/api/stats")
def stats(db: Session = Depends(get_db)):
    total_jobs = db.query(Job).count()
    total_apps = db.query(Application).count()
    selected = db.query(Application).filter(Application.status == "Selected").count()
    return {"students": 248, "companies": 32, "jobs": total_jobs, "applications": total_apps,
            "selected": selected, "placement_rate": round((selected / 248) * 100, 1)}
