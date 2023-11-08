from abc import ABC, abstractmethod


class IFabrica(ABC):    # AbstractFactory
    @abstractmethod
    def crear_televisor(self):
        pass

    @abstractmethod
    def crear_celular(self):
        pass
