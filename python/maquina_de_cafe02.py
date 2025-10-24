# ==== CONSTANTES ====
precio_pequeño = 2500
precio_mediano = 5000
precio_grande = 10000

# ==== FUNCIONES DE VALIDACIÓN ====

def es_numero_valido(entrada):
    """
    Valida si la entrada es un número entero positivo.

    Parámetros:
        entrada (str): La cadena de texto a validar

    Retorna:
        bool: True si es un número válido, False en caso contrario
    """
    if entrada == '':
        return False

    for caracter in entrada:
        if caracter not in '0123456789':
            return False

    return True


def obtener_presupuesto_valido():
    """
    Solicita al usuario un presupuesto valido hasta que ingrese un valor correcto.

    Retorna:
        int: El presupuesto valido ingresado por el usuario
    """
    while True:
        presupuesto_str = input('Digite su presupuesto: ')

        if not es_numero_valido(presupuesto_str):
            print('Por favor ingresa solo valores NUMERICOS enteros y positivos.')
            continue

        presupuesto = int(presupuesto_str)

        if presupuesto <= 0:
            print('El presupuesto debe ser mayor a 0')
            continue

        return presupuesto
    

# ==== FUNCIONES DE PROCESAMIENTO ====

def determinar_tipo_cafe(presupuesto):
    """
    Determina qué tipo de café se puede comprar con el presupuesto dado.

    Parámetros:
        presupuesto (int): El presupuesto disponible

    Retorna:
        tuple: (tipo_cafe, precio) donde tipo_cafe es str y precio es int
        Retorna (None, 0) si no alcanza para ningún café
    """
    if presupuesto >= precio_grande:
        return ("grande", precio_grande)
    elif presupuesto >= precio_mediano:
        return ("mediano", precio_mediano)
    elif presupuesto >= precio_pequeño:
        return ("pequeño", precio_pequeño)
    else:
        return (None, 0)


def calcular_cambio(presupuesto, precio_cafe):
    """
    Calcula el cambio a devolver al cliente.

    Parámetros:
        presupuesto (int): El dinero disponible del cliente
        precio_cafe (int): El precio del café seleccionado

    Retorna:
        int: La cantidad de cambio a devolver
    """
    return presupuesto - precio_cafe


# ==== FUNCIONES DE SALIDA ====

def mostrar_menu():
    """Muestra el menú de cafés disponibles con sus precios."""
    print("\n" + "="*40)
    print("         MENU DE CAFÉS DISPONIBLES")
    print("="*40)
    print(f"Café Pequeño  -  ${precio_pequeño:,}")
    print(f"Café Mediano  -  ${precio_mediano:,}")
    print(f"Café Grande   -  ${precio_grande:,}")
    print("="*40 + "\n")


def mostrar_resultado_compra(tipo_cafe, cambio):
    """
    Muestra el resultado de la compra al cliente.

    Parámetros:
        tipo_cafe (str): El tipo de café que se está preparando
        cambio (int): El cambio a devolver
    """
    print(f'\nPreparando café {tipo_cafe}')

    if cambio == 0:
        print("Gracias por su compra!")
    else:
        print(f'Su cambio es: ${cambio:,}')


def mostrar_presupuesto_insuficiente():
    """Muestra mensaje cuando el presupuesto no alcanza para ningún café."""
    print('\nNo te alcanza para ningún café')
    print(f'El café más económico cuesta ${precio_pequeño:,}')


# ==== FUNCIÓN PRINCIPAL ====

def procesar_venta_cafe(presupuesto):
    """
    Procesa la venta de café según el presupuesto del cliente.

    Parámetros:
        presupuesto (int): El presupuesto del cliente
    """
    tipo_cafe, precio_cafe = determinar_tipo_cafe(presupuesto)

    if tipo_cafe is None:
        mostrar_presupuesto_insuficiente()
    else:
        cambio = calcular_cambio(presupuesto, precio_cafe)
        mostrar_resultado_compra(tipo_cafe, cambio)


def ejecutar_programa():
    """Función principal que ejecuta todo el programa."""
    print("¡Bienvenido a la Máquina de Café!")

    mostrar_menu()

    presupuesto = obtener_presupuesto_valido()

    procesar_venta_cafe(presupuesto)

    print("\n" + "="*40)
    print("     ¡Gracias por usar nuestro servicio!")
    print("="*40)


# ==== PUNTO DE ENTRADA DEL PROGRAMA ====

if __name__== "__main__":
    ejecutar_programa()
