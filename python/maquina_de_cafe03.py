class Cafe:
    """Clase que representa un tipo de café con su tamaño y precio."""

    # Constructor de la clase Cafe
    def __init__(self, tamaño, precio):
        self.tamaño = tamaño
        self.precio = precio

    # Representación en cadena del objeto Cafe
    def __str__(self):
        """Método especial que se usa como convención para referirse al objeto mismo y str
        es un método especial que define cómo se representa el objeto como una cadena
        """
        return f"Café {self.tamaño} - ${self.precio}"


class ValidadorEntrada:
    """Clase responsable de validar la entrada del usuario."""

    @staticmethod
    def es_numerico_positivo(entrada):
        """Verifica si la entrada es un número entero positivo."""
        if entrada == '':
            return False

        for caracter in entrada:
            if caracter not in '0123456789':
                return False

        return True

    @staticmethod
    def obtener_presupuesto():
        """Solicita y valida el presupuesto del usuario."""
        while True:
            presupuesto_str = input('Digite su presupuesto: ')

            if not ValidadorEntrada.es_numerico_positivo(presupuesto_str):
                print('Por favor ingresa solo valores NUMERICOS enteros y positivos.')
                continue

            presupuesto = int(presupuesto_str)

            if presupuesto <= 0:
                print('El presupuesto debe ser mayor a 0')
                continue

            return presupuesto


class MaquinaCafe:
    """Clase que representa una máquina de café con diferentes opciones."""

    def __init__(self):
        # Inicializar los tipos de café disponibles
        self.cafes = [
            Cafe("grande", 10000),
            Cafe("mediano", 5000),
            Cafe("pequeño", 2500)
        ]

    def encontrar_cafe_disponible(self, presupuesto):
        """Encuentra el tipo de café que se puede comprar con el presupuesto."""
        for cafe in self.cafes:
            if presupuesto >= cafe.precio:
                return cafe
        return None

    def calcular_cambio(self, presupuesto, precio_cafe):
        """Calcula el cambio a devolver al cliente."""
        return presupuesto - precio_cafe

    def procesar_compra(self, presupuesto):
        """Procesa la compra del café según el presupuesto disponible."""
        cafe_seleccionado = self.encontrar_cafe_disponible(presupuesto)

        if cafe_seleccionado is None:
            print('No te alcanza para ningún café')
            return

        print(f'Preparando café {cafe_seleccionado.tamaño}')

        cambio = self.calcular_cambio(presupuesto, cafe_seleccionado.precio)

        if cambio == 0:
            print('Gracias por su compra!')
        else:
            print(f'Su cambio es: {cambio}')

    def mostrar_menu(self):
        """Muestra el menú de cafés disponibles."""
        print("\n" + "="*40)
        print("      MENÚ DE CAFÉS DISPONIBLES")
        print("="*40)
        for cafe in self.cafes:
            print(f"- {cafe}")
        print("="*40 + "\n")


class SistemaCafe:
    """Clase principal que maneja el sistema de venta de café."""

    # Constructor que inicializa la máquina de café y el validador de entrada
    def __init__(self):
        self.maquina = MaquinaCafe()
        self.validador = ValidadorEntrada()

    # Método para ejecutar el sistema de venta de café
    def ejecutar(self):
        """Ejecuta el sistema de venta de café."""
        print("¡Bienvenido a la máquina de café!")
        self.maquina.mostrar_menu()

        presupuesto = ValidadorEntrada.obtener_presupuesto()
        self.maquina.procesar_compra(presupuesto)


# Punto de entrada del programa
def main():
    sistema = SistemaCafe()
    sistema.ejecutar()


if __name__ == "__main__":
    main()