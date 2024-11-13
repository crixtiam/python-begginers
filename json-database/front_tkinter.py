# app.py
import tkinter as tk
from tkinter import messagebox
import requests

# URL de la API de FastAPI
API_URL = "http://127.0.0.1:8000"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.id_label = tk.Label(root, text="id:")
        self.id_label.pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        self.nombre_label = tk.Label(root, text="nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()

        self.apellido_label = tk.Label(root, text="apellido:")
        self.apellido_label.pack()
        self.apellido_entry = tk.Entry(root)
        self.apellido_entry.pack()

        self.edad_label = tk.Label(root, text="edad:")
        self.edad_label.pack()
        self.edad_entry = tk.Entry(root)
        self.edad_entry.pack()

        self.carrera_label = tk.Label(root, text="carrera:")
        self.carrera_label.pack()
        self.carrera_entry = tk.Entry(root)
        self.carrera_entry.pack()


        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.desc_label = tk.Label(root, text="Description:")
        self.desc_label.pack()
        self.desc_entry = tk.Entry(root)
        self.desc_entry.pack()

        self.id_label = tk.Label(root, text="ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        self.add_button = tk.Button(root, text="Add student", command=self.add_task)
        self.add_button.pack()

        self.get_button = tk.Button(root, text="Get student", command=self.get_tasks)
        self.get_button.pack()

        self.frame = tk.Frame(root, width=300, height=150, bg="lightgray")
        self.frame.place(x=50, y=50) 

        self.tasks_listbox = tk.Listbox(self.frame)
        self.tasks_listbox.pack(fill="both", expand=True)

    def add_task(self):
        
        title = self.title_entry.get()
        desc = self.desc_entry.get()
        task_id = self.id_entry.get()

        if not title or not desc or not task_id:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        task = {
            "id": int(task_id),
            "title": title,
            "description": desc,
            "completed": False
        }

        response = requests.post(f"{API_URL}/students", json=task)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Task added successfully.")
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.id_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", response.json().get("detail", "Unknown error"))

    def get_tasks(self):
        '''
        Funcion que obtiene una lista de estudiantes
        '''
        response = requests.get(f"{API_URL}/students")

        if response.status_code == 200:
            students = response.json()
            self.tasks_listbox.delete(0, tk.END)  # Limpiar la lista antes de agregar
            for student in students:
                self.tasks_listbox.insert(tk.END, f"{student['id']}: {student['nombre']} - {student['apellido']}")
        else:
            messagebox.showerror("Error", "Failed to fetch tasks.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = TaskManagerApp(root)
    root.mainloop()
