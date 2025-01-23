#Vamos a simular las ventas en un almacen de computadoras y eliminar las computadoras vendidas
class Computadora:  # Representa una computadora en una tienda

    def __init__(self, marca, modelo, precio, stock):
        # Constructor que inicializa los atributos de una computadora
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.stock = stock
        print(f" Computadora: {self.marca} {self.modelo} (Precio: ${self.precio}, Stock: {self.stock})")

    def vender(self, cantidad):
        # Simula la venta de computadoras
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Vendidas {cantidad} {self.marca} {self.modelo}(s). Stock disponibles: {self.stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad} {self.marca} {self.modelo}(s). Stock disponible: {self.stock}")

    def __del__(self):
        # Destructor que se llama cuando el objeto es eliminado
        print(f"Eliminando computadora vendida: {self.marca} {self.modelo}")


# Ejemplo de uso de la clase
if __name__ == "__main__":
    print("[INFO] Computadoras disponibles en almacen")
    laptop = Computadora("Dell", "XPS 15", 1200, 8)
    desktop = Computadora("HP", "Omen 25L", 1500, 4)

    print("[INFO] Computadoras vendidas")
    laptop.vender(2)  # Vendemos 2 computadoras
    desktop.vender(1)  # Vendemos 1 computadora

    print("[INFO] Eliminando computadoras")
    del laptop  # Llamando al destructor
    del desktop  # Llamando al destructor

    print("Fin del programa")



