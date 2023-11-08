from i_aprobador import IAprobador

class LiderTeamEjecutivo(IAprobador):
    def __init__(self):
        self._next = None

    def set_next(self, aprobador):
        self._next = aprobador

    def get_next(self):
        return self._next

    def solicitud_prestamo(self, monto):
        if 10000 < monto <= 50000:
            print("Lo manejo yo, el líder!")
        else:
            self._next.solicitud_prestamo(monto)
