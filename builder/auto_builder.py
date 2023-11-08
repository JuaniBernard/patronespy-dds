from auto import Auto

class AutoBuilder:
    def __init__(self):
        self.auto = None

    def auto(self):
        self.auto = Auto()

    def get_auto(self):
        return self.auto

    def crear_auto(self):
        self.auto = Auto()

    def build_marca(self, marca):
        pass

    def build_modelo(self, modelo):
        pass

    def build_puertas(self, puertas):
        pass

    def build_motor(self, motor):
        pass
