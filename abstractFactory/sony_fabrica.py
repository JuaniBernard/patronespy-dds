from i_fabrica import IFabrica
from sony_televisor import SonyTelevisor
from sony_celular import SonyCelular


class SonyFabrica(IFabrica):    # ConcreteFactory1
    def crear_televisor(self):
        return SonyTelevisor()

    def crear_celular(self):
        return SonyCelular()
