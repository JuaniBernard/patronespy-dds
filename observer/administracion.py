from i_libro_mal_estado import ILibroMalEstado

class Administracion(ILibroMalEstado):
    def __init__(self):
        ILibroMalEstado.__init__(self)

    def update(self):
        print('Administración: ')
        print('Envío una queja formal...')
