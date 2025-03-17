import tkinter as tk
from tkinter import ttk

# Función para convertir entre gramos, kilogramos y libras
def convertir():
    try:
        cantidad = float(entrada.get())
        unidad_origen = unidad_seleccionada.get()
        unidad_destino = unidad_destino_seleccionada.get()
        resultado_conversion.set("")

        if unidad_origen == "Gramos":
            if unidad_destino == "Kilogramos":
                resultado_conversion.set(f"{cantidad / 1000:.2f} kg")
            elif unidad_destino == "Libras":
                resultado_conversion.set(f"{cantidad * 0.00220462:.2f} lb")
            else:
                resultado_conversion.set(f"{cantidad:.2f} g")

        elif unidad_origen == "Kilogramos":
            if unidad_destino == "Gramos":
                resultado_conversion.set(f"{cantidad * 1000:.2f} g")
            elif unidad_destino == "Libras":
                resultado_conversion.set(f"{cantidad * 2.20462:.2f} lb")
            else:
                resultado_conversion.set(f"{cantidad:.2f} kg")

        elif unidad_origen == "Libras":
            if unidad_destino == "Gramos":
                resultado_conversion.set(f"{cantidad / 0.00220462:.2f} g")
            elif unidad_destino == "Kilogramos":
                resultado_conversion.set(f"{cantidad / 2.20462:.2f} kg")
            else:
                resultado_conversion.set(f"{cantidad:.2f} lb")
    except ValueError:
        resultado_conversion.set("Ingrese un número válido")

# Función para limpiar los campos
def limpiar():
    entrada.delete(0, tk.END)
    resultado_conversion.set("")

# Crear ventana
ventana = tk.Tk()
ventana.title("Conversor de Unidades de Peso")
ventana.configure(bg="#FFDDE1")
ventana.geometry("400x450")

# Etiquetas y Campo de entrada
tk.Label(ventana, text="Ingrese la cantidad:", bg="#FFC0CB", font=("Times New Roman", 12)).pack()
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Opciones de unidades de origen
tk.Label(ventana, text="Seleccione:", bg="#FFC0CB", font=("Times New Roman", 12)).pack()
unidad_seleccionada = tk.StringVar(value="Gramos")
unidades = ["Gramos", "Kilogramos", "Libras"]
menu_origen = ttk.Combobox(ventana, textvariable=unidad_seleccionada, values=unidades)
menu_origen.pack(pady=5)

# Opciones de unidades de destino
tk.Label(ventana, text="Convertir a:", bg="#FFC0CB", font=("Times New Roman", 12)).pack()
unidad_destino_seleccionada = tk.StringVar(value="Kilogramos")
menu_destino = ttk.Combobox(ventana, textvariable=unidad_destino_seleccionada, values=unidades)
menu_destino.pack(pady=5)

# Botones
tk.Button(ventana, text="Convertir", command=convertir).pack(pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=5)

# Variable de resultado
resultado_conversion = tk.StringVar()
tk.Label(ventana, text="Resultado:", bg="#FFC0CB", font=("Times New Roman", 12)).pack()
resultado_texto = tk.Text(ventana, height=3, width=30, state="disabled")
resultado_texto.pack(pady=5)

# Función para actualizar el cuadro de texto
def actualizar_resultado(*args):
    resultado_texto.config(state="normal")
    resultado_texto.delete("1.0", tk.END)
    resultado_texto.insert("1.0", resultado_conversion.get())
    resultado_texto.config(state="disabled")

resultado_conversion.trace_add("write", actualizar_resultado)

# Ejecutar ventana
ventana.mainloop()