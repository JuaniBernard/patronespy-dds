class Director:
    def __init__(self):
        self.auto_builder = None

    def get_auto_builder(self):
        return self.auto_builder.get_auto()

    def set_auto_builder(self, ab):
        self.auto_builder = ab

    def get_auto(self):
        return self.auto_builder.get_auto()

    def construct_auto(self):
        self.auto_builder.crear_auto()
        self.auto_builder.build_marca()
        self.auto_builder.build_modelo()
        self.auto_builder.build_motor()
        self.auto_builder.build_puertas()
