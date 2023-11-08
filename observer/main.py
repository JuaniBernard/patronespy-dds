from libro import Libro
from biblioteca import Biblioteca

class Main:
    def __init__(self):
        pass

if __name__ == "__main__":
    l1 = Libro("El principito")
    l1.set_estado("MALO")
    b1 = Biblioteca()
    b1.devolver_libro(l1)
