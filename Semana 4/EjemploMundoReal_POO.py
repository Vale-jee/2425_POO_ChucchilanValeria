class Pastel:
    def __init__(self, nombre, precio, sabor):
        self.nombre = nombre
        self.precio = precio
        self.sabor = sabor

    def mostrar(self):
        return f"{self.nombre} ({self.sabor}) - ${self.precio:.2f}"

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.ordenes = []

    def hacer_pedido(self, orden):
        self.ordenes.append(orden)

class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.pasteles = []
        self.total = 0

    def agregar_pastel(self, pastel):
        self.pasteles.append(pastel)
        self.total += pastel.precio

    def mostrar(self):
        detalles = f"Orden de {self.cliente.nombre} ({self.cliente.telefono}):\n"
        for pastel in self.pasteles:
            detalles += f"- {pastel.mostrar()}\n"
        detalles += f"Total: ${self.total:.2f}"
        return detalles

# Creando pasteles
pastel_vainilla = Pastel("Pastel de Vainilla", 12.50, "Vainilla")
pastel_chocolate = Pastel("Pastel de Chocolate", 15.00, "Chocolate")

# Creando cliente y su orden
cliente_ana = Cliente("Ana López", "0997654321")
orden_ana = Orden(cliente_ana)

# Cliente realiza pedido
orden_ana.agregar_pastel(pastel_vainilla)
orden_ana.agregar_pastel(pastel_chocolate)
cliente_ana.hacer_pedido(orden_ana)

# Mostrar detalles del pedido
print(orden_ana.mostrar())