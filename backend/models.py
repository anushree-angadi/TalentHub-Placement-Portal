from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String, default="India")
    package = Column(Float, default=0)
    min_cgpa = Column(Float, default=0)
    description = Column(String, default="")
    status = Column(String, default="Open")

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String, nullable=False)
    student_email = Column(String, nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    status = Column(String, default="Applied")
