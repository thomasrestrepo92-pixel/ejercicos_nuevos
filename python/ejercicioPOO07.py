class figura:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


class circulo(figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio * self.radio
    
    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio
    

class rectangulo(figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2* (self.base + self.altura)
    

class triangulo(figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        return (self.base * self.altura) /2
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    

figuras=[
    circulo(5),
    rectangulo(4, 6),
    triangulo(4, 3, 4, 3, 5)
]

area_total = 0
for figura in figuras:
    print(f"{figura.__class__.__name__},area:{figura.calcular_area()},perimetro:{figura.calcular_perimetro()}")
    area_total += figura.calcular_area()

print(f"area total de las figuras {area_total}")