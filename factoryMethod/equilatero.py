from triangulo import Triangulo

class Equilatero(Triangulo):
    def __init__(self, ladoA, ladoB, ladoC):
        super().__init__(ladoA, ladoB, ladoC)

    def get_descripcion(self):
        return "Soy un triángulo Equilátero"

    def get_superficie(self, base, altura):
        return 0

    def dibujate(self):
        pass
