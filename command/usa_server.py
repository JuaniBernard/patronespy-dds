from i_server import IServer
# Clase USAServer
class USAServer(IServer):
    def apagate(self):
        print("Apagando el servidor de USA")

    def cierra_conexion(self):
        print("Cerrando conexion con el servidor de USA")

    def conectate(self):
        print("Conectando al servidor de USA")

    def guarda_log(self):
        print("Guardar Log de USA")

    def prendete(self):
        print("Prendiendo el servidor de USA")

    def verifica_conexion(self):
        print("Verificando conexión de USA")
