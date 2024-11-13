import json

class Student:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.carrera = None

    def get_students(self)->list:
        '''
        return: retorna lista de estudiantes (cada valor de estudiante lo trae como diccionario)
        '''
        try:
            with open('../../json-database/files/students.json', 'r') as file:
                students = json.load(file)
        except FileNotFoundError:
            students = []
        return students
    