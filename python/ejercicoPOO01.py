# definimos una clase llamada perro
class perro:
    #metodo constructor: inicializa los atributos del perro
    def __init__(self , nombre , edad):
        #inicializamos los atributos del perrro
        self.nombre = nombre 
        self.edad = edad

    # metodos de la clase perro
    def comer(self):
        """metodo que simula al perro comiendo"""
        print(f"{self.nombre} esta comiendo su comida favorita")

    def ladrar(self):
        """metodo que simula el perro ladrando"""
        print(f"{self.nombre} dice :¡guau , guau!")

    def presentarse(self):
        """metodo que presenta al perro"""
        print(f"hola , soy {self.nombre} y tengo {self.edad} años")

    def correr(self):
        """metodo que simula el perro corriendo"""
        print(f"hola soy {self.nombre} y corro muy rapido")        

#creamos un objeto (instancia de la clase)
if __name__ == "__main__":
    mi_perro = perro("pancho", 4)
    mi_perro.presentarse()
    mi_perro.comer()
    mi_perro.ladrar()
    mi_perro.correr()