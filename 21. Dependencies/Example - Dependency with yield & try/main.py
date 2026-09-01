from fastapi import FastAPI, Depends
from database import DBSession, Base, engine
from models import Student
from pydantic import BaseModel

app = FastAPI()
Base.metadata.create_all(bind=engine)

class CreateStudent(BaseModel):
    name: str
    age: int

async def get_db():     # Dependency used by all endpoints
    db = DBSession()
    try:
        yield db
    finally:
        db.close()

@app.get('/student/', tags=['All Students'])
async def get_students(db = Depends(get_db)):
    students = db.query(Student).all()
    return students

@app.get('/student/{student_id}', tags=['Get Student'])
async def get_student(student_id: int, db = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    return student

@app.delete('/student/{student_d}', tags=['Delete Student'])
async def delete_student(student_id: int, db = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    db.delete(student)
    db.commit()
    return {"message": "Student deleted!"}

@app.post('/student/', tags=['Add Student'])
async def add_students(student: CreateStudent, db = Depends(get_db)):
    new_student = Student(name = student.name, age = student.age)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student added!"}