class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open("inventario.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        producto = Producto(datos[0], datos[1], int(datos[2]), float(datos[3]))
                        self.productos.append(producto)
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
        except PermissionError:
            print("Error: No se tienen permisos para acceder al archivo de inventario.")

    def guardar_en_archivo(self):
        try:
            with open("inventario.txt", "w") as archivo:
                for p in self.productos:
                    archivo.write(f"{p.producto_id},{p.nombre},{p.cantidad},{p.precio}\n")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo de inventario.")

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.producto_id == producto.producto_id:
                print("Error: El producto ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto añadido correctamente.")

    def eliminar_producto(self, producto_id):
        self.productos = [p for p in self.productos if p.producto_id != producto_id]
        self.guardar_en_archivo()
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        for p in self.productos:
            if p.producto_id == producto_id:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return resultados if resultados else "No se encontraron productos."

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Inventario de Joyas de Oro y Plata ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto_id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(Producto(producto_id, nombre, cantidad, precio))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")

        elif opcion == "2":
            producto_id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)

        elif opcion == "3":
            producto_id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(producto_id, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if isinstance(resultados, list):
                for r in resultados:
                    print(r)
            else:
                print(resultados)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
