from main_test import MainTest
from samsung_fabrica import SamsungFabrica
from sony_fabrica import SonyFabrica


class Main:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config = Main.read_application_config_file()

        if config["Fábrica"] == "Sony":
            fabrica = SonyFabrica()
        elif config["Fábrica"] == "Samsung":
            fabrica = SamsungFabrica()
        else:
            raise Exception("Error! Fábrica desconocida.")

        print("Fábrica: " + config["Fábrica"])
        app = MainTest(fabrica)
        app.fabricar_tv()
        app.actua_tv()
        app.fabricar_celular()
        app.actua_celular()

    @staticmethod
    def read_application_config_file():
        # Simular la lectura de la configuración desde un archivo
        return {"Fábrica": "Samsung"}  # Cambiar la fábrica según sea necesario

# Ejecutar la aplicación
if __name__ == "__main__":
    Main.main()
