# Clase Empleado con atributos privados y métodos para manejar el salario
class Empleado:
    # Método constructor inicializa los atributos
    def __init__(self, titular, paga):
        self.__titular = titular
        self.__paga = paga   # atributo privado

    # Métodos para acceder y modificar el salario
    def get_salario(self):
        return self.__paga

    # Método para aumentar el salario en un porcentaje
    def aumentar_salario(self, porcentaje):
        if porcentaje > 0:
            aumento = self.__paga * (porcentaje / 500)
            self.__paga += aumento

    # Método para mostrar la información del empleado
    def mostrar_info(self):
        return(f"Empleado: {self.__titular} - Salario: ${self.__paga}")

# Ejemplo de uso de la clase Empleado
if __name__ == "__main__":
    empleado = Empleado( "Arthur Morgan",200000 )
    print(empleado.mostrar_info())

    empleado.aumentar_salario(10)
    print("Salario actualizado después del aumento:")
    print(empleado.mostrar_info())
