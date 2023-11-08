from director import Director
from ejecutivo_de_cuenta import EjecutivoDeCuenta
from gerente import Gerente
from i_aprobador import IAprobador
from lider_team_ejecutivo import LiderTeamEjecutivo


class Banco(IAprobador):
    def __init__(self):
        self._next = None

    def set_next(self, aprobador):
        self._next = aprobador

    def get_next(self):
        return self._next

    def solicitud_prestamo(self, monto):
        ejecutivo = EjecutivoDeCuenta()
        self.set_next(ejecutivo)

        lider = LiderTeamEjecutivo()
        ejecutivo.set_next(lider)

        gerente = Gerente()
        lider.set_next(gerente)

        director = Director()
        gerente.set_next(director)

        self._next.solicitud_prestamo(monto)
