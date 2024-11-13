from fastapi import FastAPI #, HTTPException
#from enum import Enum
#from pydantic import BaseModel
from student import Student

app = FastAPI()

#class StudentModel(BaseModel):
#    id: int
#    nombre: str
#    apellido: str
#    edad: int
#    carrera: str

students_db = Student()

# GET, POST, PUT, DELETE

@app.get("/students")
async def get_students():
    #comunicacion con los datos
    students_list = students_db.get_students()
    return students_list