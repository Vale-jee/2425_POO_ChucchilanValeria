class ClimaQuito:
    def __init__(self):
        """
        Inicializa la clase con un atributo privado para las temperaturas diarias.
        """
        # Temperaturas en Quito (en grados Celsius)
        self.__temperaturas = [15.5, 16.0, 14.8, 15.2, 15.9, 16.3, 15.1]  # datos siete días

    def mostrar_temperaturas(self):
        """
        Método para mostrar las temperaturas registradas.
        """
        print("Temperaturas registradas en Quito durante la semana (en °C):")
        for dia, temp in enumerate(self.__temperaturas, start=1):
            print(f"Día {dia}: {temp}°C")

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal de las temperaturas.
        """
        suma = sum(self.__temperaturas)
        promedio = suma / len(self.__temperaturas)
        return promedio


class ClimaResumen(ClimaQuito):
    """
    Clase que hereda de ClimaQuito para agregar funcionalidades adicionales.
    """
    def mostrar_resumen(self):
        """
        Método para mostrar un resumen de las temperaturas y el promedio semanal.
        """
        self.mostrar_temperaturas()
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de las temperaturas en Quito es: {promedio:.2f}°C")


def main():
    print("Cálculo del promedio semanal de temperaturas en Quito utilizando POO.")
    clima = ClimaResumen()  # Instanciar la clase
    clima.mostrar_resumen()  # Mostrar el resumen de temperaturas y promedio


if __name__ == "__main__":
    main()