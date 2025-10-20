estudiantes=[]
while True:
    nombre=input("ingrese nombre: ")
    if nombre.lower() == "salir":
        print("no asistieron mas ", estudiantes)
        break
    estudiantes.append(nombre)
    print("estudiate resgistrado:", estudiantes)