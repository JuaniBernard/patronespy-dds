from i_libro_mal_estado import ILibroMalEstado

class Stock(ILibroMalEstado):
    def __init__(self):
        ILibroMalEstado.__init__(self)

    def update(self):
        print('Stock: ')
        print('Le doy de baja...')
