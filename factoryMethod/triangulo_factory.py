from isosceles import Isosceles
from equilatero import Equilatero
from escaleno import Escaleno
from i_triangulo_factory_method import ITrianguloFactoryMethod

class TrianguloFactory(ITrianguloFactoryMethod):
    def create_triangulo(self, ladoA, ladoB, ladoC):
        if ladoA == ladoB == ladoC:
            return Equilatero(ladoA, ladoB, ladoC)
        elif ladoA != ladoB != ladoC != ladoA:
            return Escaleno(ladoA, ladoB, ladoC)
        else:
            return Isosceles(ladoA, ladoB, ladoC)
