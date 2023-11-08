from abc import ABC, abstractmethod


class ITelevisor(ABC):    # ProductA
    @abstractmethod
    def funcion_televisor(self):
        pass
