class MainTest:
    def __init__(self, fabrica):
        self.fabrica = fabrica

    def fabricar_tv(self):
        self.televisor = self.fabrica.crear_televisor()

    def fabricar_celular(self):
        self.celular = self.fabrica.crear_celular()

    def actua_tv(self):
        print(self.televisor.funcion_televisor())

    def actua_celular(self):
        print(self.celular.funcion_celular())
