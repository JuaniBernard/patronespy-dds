from i_command import ICommand
# Clase ResetServer
class ResetServer(ICommand):
    def __init__(self, servidor):
        self.servidor = servidor

    def execute(self):
        self.servidor.conectate()
        self.servidor.verifica_conexion()
        self.servidor.guarda_log()
        self.servidor.apagate()
        self.servidor.prendete()
        self.servidor.guarda_log()
        self.servidor.cierra_conexion()
