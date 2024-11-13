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

        self.get_button = tk.Button(root, text="Get student", command=self.get_tasks)
        self.get_button.pack()

        self.frame = tk.Frame(root, width=300, height=150, bg="lightgray")
        self.frame.place(x=50, y=50) 

        self.tasks_listbox = tk.Listbox(self.frame)
        self.tasks_listbox.pack(fill="both", expand=True)
    
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
