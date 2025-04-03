import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def mark_completed():
    try:
        selected_index = task_list.curselection()[0]
        task = task_list.get(selected_index)
        task_list.delete(selected_index)
        task_list.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def close_app(event=None):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")
root.configure(bg="#D8BFD8")  # Color lila rosa

# Campo de entrada
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)

# Lista de tareas
task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=10)

# Botones
button_frame = tk.Frame(root, bg="#D8BFD8")  # Color de fondo del frame
button_frame.pack()

add_button = tk.Button(button_frame, text="Añadir", command=add_task, bg="#F4C2C2")  # Rosa palo
add_button.grid(row=0, column=0, padx=5)

complete_button = tk.Button(button_frame, text="Completar", command=mark_completed, bg="#F4C2C2")  # Rosa palo
complete_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Eliminar", command=delete_task, bg="#F4C2C2")  # Rosa palo
delete_button.grid(row=0, column=2, padx=5)

# Atajos de teclado
root.bind("c", lambda event: mark_completed())
root.bind("d", lambda event: delete_task())
root.bind("<Delete>", lambda event: delete_task())
root.bind("<Escape>", close_app)

# Ejecutar la aplicación
root.mainloop()
