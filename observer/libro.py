class Libro:
    def __init__(self, titulo=None, estado=None):
        self.titulo = titulo
        self.estado = estado

    def get_titulo(self):
        return self.titulo

    def get_estado(self):
        return self.estado

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_estado(self, estado):
        self.estado = estado
