from abc import ABC, abstractmethod
# Interfaz Command
class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass
