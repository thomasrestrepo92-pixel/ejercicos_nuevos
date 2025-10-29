class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentacion(self):
        return f"hola me llamo {self.nombre} y tengo {self.edad}"

    def cumpleaños(self):
        self.edad += 1

persona1 = persona("jhon", 22)
persona2 = persona("arthur", 33)

print(persona1.presentacion())
print(persona2.presentacion())

persona1.cumpleaños()
persona2.cumpleaños()

print(persona1.presentacion())
print(persona2.presentacion())
