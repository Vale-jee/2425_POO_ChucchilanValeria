import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            "ID": self.id_producto,
            "Nombre": self.nombre,
            "Cantidad": self.cantidad,
            "Precio": self.precio
        }

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
            self.guardar_en_archivo()
            print("Producto agregado:")
            print(self.productos[id_producto])

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for producto in sorted(self.productos.values(), key=lambda p: p.nombre):
                print(producto)

    def guardar_en_archivo(self):
        try:
            with open("inventario.json", "w") as archivo:
                json.dump([p.to_dict() for p in self.productos.values()], archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = {p["ID"]: Producto(p["ID"], p["Nombre"], p["Cantidad"], p["Precio"]) for p in datos}
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo al guardar.")
            self.productos = {}
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. Asegúrese de que el formato sea correcto.")
            self.productos = {}


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto\n2. Eliminar producto\n3. Actualizar producto\n4. Mostrar inventario ordenado\n5. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            inventario.mostrar_productos()

        elif opcion == "5":
            inventario.guardar_en_archivo()
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
