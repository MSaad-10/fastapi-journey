from sqlalchemy import Column, String, Integer
from database import Base


class Student(Base):
    __tablename__ = "Students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)