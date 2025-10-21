estudiante={

}

estudiante[input("Ingrese el nombre del estudiante: ")] = float(input("Ingrese la calificación del estudiante: "))
while True:
    nombre=input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    calificacion=float(input("Ingrese la calificación del estudiante: "))
    estudiante[nombre] = calificacion

for nombre, calificacion in estudiante.items():
    print(f"{nombre}: {calificacion}")

total=0
for calificacion in estudiante.values():
    total += calificacion
promedio = total / len(estudiante)
print(f"Promedio de calificaciones: {promedio}")