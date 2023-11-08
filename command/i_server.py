from abc import ABC, abstractmethod
# Interfaz IServer
class IServer(ABC):
    @abstractmethod
    def apagate(self):
        pass

    @abstractmethod
    def prendete(self):
        pass

    @abstractmethod
    def conectate(self):
        pass

    @abstractmethod
    def verifica_conexion(self):
        pass

    @abstractmethod
    def guarda_log(self):
        pass

    @abstractmethod
    def cierra_conexion(self):
        pass
