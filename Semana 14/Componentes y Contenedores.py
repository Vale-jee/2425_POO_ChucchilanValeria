import tkinter as tk     # Biblioteca para la interfaz gráfica
from tkinter import ttk, messagebox     # Modulos para usar componentes de la interfaz y mostrar mensajes de advertencia
from tkcalendar import Calendar     # Para usar un calendario en la interfaz

# Definición de la clase principal para la aplicación de la agenda
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x700")

        # Creación de un calendario en la ventana para seleccionar fechas
        self.calendario = Calendar(self.root, selectmode='day', year=2025, month=3, day=19)
        self.calendario.pack(pady=10)

        # Frame para la lista de eventos
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=0, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada, width=15)
        self.hora_entry.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0)
        self.desc_entry = tk.Entry(self.frame_entrada, width=30)
        self.desc_entry.grid(row=1, column=1)

        # Frame para los botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1,
                                                                                                 padx=5)
        tk.Button(self.frame_botones, text="Salir", command=self.root.quit).grid(row=0, column=2, padx=5)

    # Método para agregar un evento a la lista de eventos
    def agregar_evento(self):
        fecha = self.calendario.get_date()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.hora_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Inválida", "Todos los campos son obligatorios")

    # Método para eliminar un evento seleccionado de la lista
    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmación", "¿Seguro que deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Selección Inválida", "Selecciona un evento para eliminar")

# Bloque principal de la aplicación, se ejecuta al iniciar el programa
if __name__ == "__main__":
    root = tk.Tk()     # Crear la ventana principal
    app = AgendaApp(root)     # Crear una instancia de la clase AgendaApp
    root.mainloop()     # Iniciar el bucle de eventos de la interfaz gráfica

