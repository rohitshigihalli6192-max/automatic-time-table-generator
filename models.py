from extensions import db
from sqlalchemy.orm import relationship

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(120))
    subjects = db.Column(db.String(500))
    availability = db.Column(db.String(500))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    hours_per_week = db.Column(db.Integer, default=0)
    faculty = relationship('Faculty', backref='courses')

class TimetableSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(30), nullable=False)
    period = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    faculty = relationship('Faculty')
    course = relationship('Course')
