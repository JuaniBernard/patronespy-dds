from argentina_server import ArgentinaServer
from invoker import Invoker
from prender_server import PrenderServer
class Main:
    def __init__(self):
        pass

if __name__ == "__main__":
    command = PrenderServer(ArgentinaServer())
    server_admin = Invoker(command)
    server_admin.run()
