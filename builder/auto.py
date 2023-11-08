class Auto:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.cantidad_puertas = 0
        self.motor = None

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_cantidad_puertas(self, cantidad_puertas):
        self.cantidad_puertas = cantidad_puertas

    def set_motor(self, motor):
        self.motor = motor

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Puertas: {self.cantidad_puertas}, Motor: {self.motor}"
