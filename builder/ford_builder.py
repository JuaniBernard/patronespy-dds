from auto_builder import AutoBuilder
from motor import Motor

class FordBuilder(AutoBuilder):
    def build_marca(self):
        self.auto.set_marca("Ford")

    def build_modelo(self):
        self.auto.set_modelo("Explorer")

    def build_puertas(self):
        self.auto.set_cantidad_puertas(4)

    def build_motor(self):
        motor = Motor()
        motor.set_numero(124)
        motor.set_potencia("25HP")
        self.auto.set_motor(motor)
