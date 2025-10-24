pequeño = 2500
mediano = 5000
grande = 10000

#validacion de entrada : aceptar solo numeros enteros positivos
while True:
    presupuesto= input('digite su presupuesto: ')

    #verificar que todos los caracteres sean digitos 0-9
    es_numerico = True
    if presupuesto == '':
        es_numerico= False
    else:
        for caracter in presupuesto:
            if caracter not in '0123456789':
                es_numerico = False
                break

    if not es_numerico:
        print('por favor ingresa solo valores NUMERICOS enteros y positivos.')
        continue

    presupuesto = int(presupuesto)
    break

if presupuesto > 0:
    if presupuesto >= grande:
        print('preparando cafe grande')
        if presupuesto == grande:
            print(' gracias por su compra!')
        else:
            print('su cambio es' , presupuesto - grande)
    elif presupuesto == mediano:
        print('preparando cafe mediano')
        print('gracias por su compra!')
    elif presupuesto >= pequeño:
        print('preparando cafe pequeño')
        if presupuesto == pequeño:
            print('gracias por su compra!')
        else:
            print('su cambio es: ', presupuesto - pequeño)
    else:
            print(' no te alcanza para ningun cafe')
else:
    print('el presupuesto debe de ser mayor a 0')
