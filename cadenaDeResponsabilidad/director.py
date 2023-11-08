from i_aprobador import IAprobador

class Director(IAprobador):
    def __init__(self):
        self._next = None

    def set_next(self, aprobador):
        self._next = aprobador

    def get_next(self):
        return self._next

    def solicitud_prestamo(self, monto):
        if monto > 100000:
            print("Lo manejo yo, el director!")
