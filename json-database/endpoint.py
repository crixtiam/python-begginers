from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel
from students import Students

app = FastAPI()

class StudentModel(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int
    carrera: str

students_db = Students()

@app.get("/students")
async def get_students():
    students_list = students_db.get_students()
    return students_list