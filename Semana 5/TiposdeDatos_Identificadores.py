# Este programa gestiona una lista de productos con sus precios y cantidades.
# Calcula el total de la compra según los productos seleccionados y sus cantidades.

def calcular_total_compra(productos):
    total = 0
    for producto in productos:
        total += producto['precio'] * producto['cantidad']
    return total

def mostrar_lista_de_productos():
    return [
        {'nombre': 'Yogurt', 'precio': 1.2, 'cantidad': 0},
        {'nombre': 'Leche', 'precio': 0.8, 'cantidad': 0},
        {'nombre': 'Queso', 'precio': 1.5, 'cantidad': 0},
        {'nombre': 'Aceite', 'precio': 2.0, 'cantidad': 0}
    ]


# Mostrar los productos disponibles
productos_disponibles = mostrar_lista_de_productos()
print("Productos disponibles:")
for producto in productos_disponibles:
    print(f"- {producto['nombre']} a ${producto['precio']} por unidad")

# Solicitar al usuario las cantidades de los productos
for producto in productos_disponibles:
    cantidad = int(input(f"¿Cuántas unidades de {producto['nombre']} deseas comprar? "))
    producto['cantidad'] = cantidad

# Calcular el total de la compra
total = calcular_total_compra(productos_disponibles)
print(f"\nEl total de tu compra es: ${total:.2f}")