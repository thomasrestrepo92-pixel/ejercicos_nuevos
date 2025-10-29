class gato:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad
        
    def comer(self):
        """metodo que simula al gato comiendo"""
        print(f"{self.nombre} esta comiedo reposadito")

    def maullar(self):
        """metodo que simula el gato maullando"""
        print(f"{self.nombre} dice : miauuuu")

    def saltar(self):
        """metodo que simula el gato saltando"""
        print(f"{self.nombre} salta muy alto")

if __name__ == "__main__":
    mi_gato = gato("cucho" , 3)
    mi_gato.comer()
    mi_gato.maullar()
    mi_gato.saltar()