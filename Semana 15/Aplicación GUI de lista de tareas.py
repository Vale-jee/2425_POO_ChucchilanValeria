import tkinter as tk
from tkinter import ttk, messagebox

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        tree.insert("", tk.END, values=(tarea,))
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Debe ingresar una tarea")

def marcar_completada():
    try:
        seleccion = tree.selection()[0]
        tarea = tree.item(seleccion, "values")[0]
        tree.item(seleccion, values=(f"✔ {tarea}",))
    except IndexError:
        messagebox.showwarning("Aviso", "Debe seleccionar una tarea")

def eliminar_tarea():
    try:
        seleccion = tree.selection()[0]
        tree.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Aviso", "Debe seleccionar una tarea")

def agregar_con_enter(event):
    agregar_tarea()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")
root.configure(bg="#E0F2F1")  # Fondo de la ventana en turquesa menta pastel

# Entrada de tarea
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_con_enter)

# Botones
btn_color = "#A7DBD8"  # Turquesa más bajo para los botones
btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea, bg=btn_color, fg="black")
btn_agregar.pack()
btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada, bg=btn_color, fg="black")
btn_completar.pack()
btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea, bg=btn_color, fg="black")
btn_eliminar.pack()

# Treeview para lista de tareas
style = ttk.Style()
style.configure("Treeview", background="#E0F2F1", fieldbackground="#E0F2F1", foreground="black")
tree = ttk.Treeview(root, columns=("Tarea",), show="headings")
tree.heading("Tarea", text="Tarea")
tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Ejecutar aplicación
root.mainloop()
