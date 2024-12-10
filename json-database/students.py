import json

class Students:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.carrera = None

    def get_students(self):
        try:
            with open('./files/students.json', 'r') as file:
                students = json.load(file)
        except FileNotFoundError:
            students = []
        return students
    #def __str__(self):
    #    return f'{self.id} {self.nombre} {self.apellido} {self.edad} {self.carrera}'
#
    #def __repr__(self):
    #    return self.__str__()