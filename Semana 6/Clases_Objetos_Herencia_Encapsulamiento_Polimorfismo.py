#Clases, objetos, herencia, encapsulamiento y polimorfismo
# Ejemplo que representa y gestiona productos de joyeria
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Atributo público
        self.__precio = precio  # Atributo privado (encapsulacion)

    def obtener_precio(self):
        return self.__precio

    def detalles(self):
        return f"{self.nombre} cuesta ${self.__precio}"


# Clase derivada: Joya (hereda de Producto)
class Joya(Producto):
    def __init__(self, nombre, precio, metal):
        super().__init__(nombre, precio)  # Llamada al constructor de la clase base
        self.metal = metal  # Nuevo atributo específico de Joya

    # Sobrescribe el método detalles de la clase base
    def detalles(self):
        return f"{self.nombre} de {self.metal} cuesta ${self.obtener_precio()}"


# Crear instancias y mostrar detalles
producto = Producto("Anillo", 500)  # Instancia de la clase base
joya = Joya("Collar", 1200, "Oro")  # Instancia de la clase derivada

print(producto.detalles())  # Llamada al método de la clase base
print(joya.detalles())  # Llamada al método sobrescrito en la clase derivada