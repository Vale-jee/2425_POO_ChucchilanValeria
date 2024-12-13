# Función para ingresar temperaturas de Quito
def ingresar_temperaturas():
    """
    Función que devuelve las temperaturas de Quito para 7 días.
    """
    # Temperaturas de Quito(en grados Celsius)
    temperaturas = [15.5, 16.0, 14.8, 15.2, 15.9, 16.3, 15.1]  # Datos de siete días
    print("Temperaturas registradas en Quito durante la semana (en °C):")
    for dia, temp in enumerate(temperaturas, start=1):
        print(f"Día {dia}: {temp}°C")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función principal para organizar el flujo del programa
def main():
    print("Cálculo del promedio semanal de temperaturas en Quito.")
    temperaturas = ingresar_temperaturas()  # Obtener las temperaturas reales
    promedio = calcular_promedio_semanal(temperaturas)  # Calcular el promedio
    print(f"\nEl promedio semanal de las temperaturas en Quito es: {promedio:.2f}°C")

# Llamar a la función principal
if __name__ == "__main__":
    main()