#clase base : animal 
class animal:
    #metodo constructor :define los atributos comunes
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #metodo comun para presentar al animal
    def presentar(self):
        print(f"hola, soy {self.nombre} y tengo {self.edad} años.")

#subclase: perro (hereda animal)
class perro(animal):
    def __init__(self, nombre, edad):
        #llama al constructor de la clase padre(animal)
        super().__init__(nombre, edad)

    #metodo propio del perro
    def comer(self):
        print(f"{self.nombre} esta comiendo su comida favorita")

#subclase: gato ( hereda animal)
class gato(animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    # metodo propio de gato
    def caminar(self):
        print(f"{self.nombre} esta caminando silenciosamente")

#creacion de los objetos (instancias)
perro = perro("pancho", 4)
gato = gato("paco", 3)

#uso de los metodos
perro.presentar() #metodo heredado de animal
perro.comer() # metodo propio de perro

gato.presentar #metodo heredado de animal
gato.caminar #metodo propio de animal
