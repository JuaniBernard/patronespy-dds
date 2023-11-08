from i_fabrica import IFabrica
from samsung_televisor import SamsungTelevisor
from samsung_celular import SamsungCelular


class SamsungFabrica(IFabrica):    # ConcreteFactory2
    def crear_televisor(self):
        return SamsungTelevisor()

    def crear_celular(self):
        return SamsungCelular()
