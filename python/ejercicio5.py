def programa_ahorro():
    print("Bienvenido al programa de ahorro personal.")

    try:
        meta = float(input("Ingresa tu meta de ahorro: $"))
        if meta <= 0:
            print("La meta debe ser un número mayor a 0.")
            return
    except ValueError:
        print("Por favor ingresa un número válido.")
        return

    ahorro_total = 0.0
    meses = 0

    while ahorro_total < meta:
        try:
            cantidad = float(input(f"Ingreso del mes {meses + 1}: $"))
            if cantidad < 0:
                print("No puedes ingresar un valor negativo.")
                continue
            ahorro_total += cantidad
            meses += 1
            print(f"Ahorro acumulado: ${ahorro_total:.2f}\n")
        except ValueError:
            print("Por favor ingresa un número válido.")

    print("Felicidades, Has alcanzado tu meta de ahorro.")
    print(f"Te tomó {meses} mes(es) ahorrar ${ahorro_total:.2f}.")

programa_ahorro()
