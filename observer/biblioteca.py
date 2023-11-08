from alarma_libro import AlarmaLibro
from stock import Stock
from administracion import Administracion
from compras import Compras

class Biblioteca:
    def devolver_libro(self, libro):
        if libro.get_estado() == "MALO":
            a = AlarmaLibro()
            a.attach(Stock)
            a.attach(Administracion)
            a.attach(Compras)
            print("Rompieron el libro:", libro.get_titulo())
            a.notify_observers()
        elif libro.get_estado() == "BUENO":
            print("El libro -", libro.get_titulo(), "- fue devuelto en buen estado.")
        else:
            print("El estado ingresado es incorrecto. Ingrese BUENO o MALO.")
