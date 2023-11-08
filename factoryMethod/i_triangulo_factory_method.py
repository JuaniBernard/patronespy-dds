from abc import ABC, abstractmethod

class ITrianguloFactoryMethod(ABC):
    @abstractmethod
    def create_triangulo(self, ladoA, ladoB, ladoC):
        pass
