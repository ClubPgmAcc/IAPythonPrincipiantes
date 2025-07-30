# Convierte de Programación estructurada a POO
# Transforma este código en un conjunto de clases 
# (Triangulo y Rectángulo) que tengan métodos para calcular su área.

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2
    
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

triangulo = Triangulo(5, 8)
calcular_area_triangulo = triangulo.calcular_area()
print(f"Área del triángulo: {calcular_area_triangulo}")

rectangulo = Rectangulo(6, 4)
calcular_area_rectangulo = rectangulo.calcular_area()
print(f"Área del rectángulo: {calcular_area_rectangulo}")

