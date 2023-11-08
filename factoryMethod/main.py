from triangulo_factory import TrianguloFactory
from i_triangulo_factory_method import ITrianguloFactoryMethod

class Main:
    def __init__(self):
        pass

if __name__ == "__main__":
    metodo: ITrianguloFactoryMethod = TrianguloFactory()
    triangulo = metodo.create_triangulo(10, 10, 10)

    print(triangulo.get_descripcion())
