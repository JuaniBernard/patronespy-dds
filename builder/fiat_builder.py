from auto_builder import AutoBuilder
from motor import Motor

class FiatBuilder(AutoBuilder):
    def build_marca(self):
        self.auto.set_marca("Fiat")

    def build_modelo(self):
        self.auto.set_modelo("Pulse")

    def build_puertas(self):
        self.auto.set_cantidad_puertas(2)

    def build_motor(self):
        motor = Motor()
        motor.set_numero(123)
        motor.set_potencia("23HP")
        self.auto.set_motor(motor)
