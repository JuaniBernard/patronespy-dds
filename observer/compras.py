from i_libro_mal_estado import ILibroMalEstado

class Compras(ILibroMalEstado):
    def __init__(self):
        ILibroMalEstado.__init__(self)

    def update(self):
        print('Compras: ')
        print('Solicito una nueva cotización...')
