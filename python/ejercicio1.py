while True:
    numero=float(input("ingrese su valor"))
    cambio=4.000
    try:
        num= int(numero)
        if num  >=  1 :
            print(f"su {num} es valido pra cambiar")
            cambio=num/cambio
            print(f"su valor en dolares es {cambio}")
            break
        else:
            print(f"tu {num} no se puede comvertir")
    except ValueError:
        print("ingrese un valor real")
        
