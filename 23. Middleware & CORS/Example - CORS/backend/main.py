from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, ConfigDict, Field, field_validator
from fastapi.middleware.cors import CORSMiddleware
from database import Base, DBSession, engine
from model import Student

app = FastAPI(title='Student CORS API')
Base.metadata.create_all(bind=engine)

# Allowed Origins
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['GET', 'POST', 'DELETE', 'OPTIONS'],
    allow_headers=['Content-Type'],
    allow_credentials=True
)

# CreateStudent Class
class CreateStudent(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=1, le=150)

    @field_validator('name')
    @classmethod
    def clean_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError('Name cannot be blank')
        return value

class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    age: int

# Dependency
async def get_db():     
    db = DBSession()
    try:
        yield db
    finally:
        db.close()

# Health Check Endpoint
@app.get('/', tags=['health'])
async def health_check() -> dict['str', 'str']:
    return {"message": "Student API is running"}

# Add Student Endpoint
@app.post('/students', response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=["Add Student"])
async def add_student(student: CreateStudent, db = Depends(get_db)) -> StudentResponse:
    new_student = Student(name = student.name, age = student.age)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Search Student Endpoint
@app.get('/students/{student_id}', response_model=StudentResponse, tags=['Search Student'])
async def get_student(student_id: int, db = Depends(get_db)) -> StudentResponse:
    student = db.query(Student).filter(Student.id == student_id).first()
    return student

# All Students Endpoint
@app.get('/students', tags=['All Students'])
async def get_students(db = Depends(get_db)):
    students = db.query(Student).all()
    return students

# Delete Student
@app.delete('/students/{student_id}', tags=['Delete Student'], status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int, db = Depends(get_db)) -> None:
    student = db.query(Student).filter(Student.id == student_id).first()
    db.delete(student)
    db.commit()