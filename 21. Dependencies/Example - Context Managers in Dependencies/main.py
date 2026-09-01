from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Annotated
from database import Base, engine, get_db
from models import Student


app = FastAPI()

# Create Database tables
Base.metadata.create_all(bind=engine)

# Pydantic model
class CreateStudent(BaseModel):
    name: str
    age: int

@app.post('/students/', tags=['Create Students'])
async def create_student(student: CreateStudent, db: Annotated[object, Depends(get_db)]):
    new_student = Student(name = student.name, age = student.age)
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "id": new_student.id,
        "name": new_student.name,
        "age": new_student.age
    }

@app.get('/students/', tags=['Get Students'])
async def get_students(db: Annotated[object, Depends(get_db)]):
    students = db.query(Student).all()
    return students