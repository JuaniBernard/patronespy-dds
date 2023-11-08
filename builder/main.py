from director import Director
from ford_builder import FordBuilder

class Main:
    def __init__(self):
        pass

if __name__ == "__main__":
    director = Director()
    auto_ford = FordBuilder()
    director.set_auto_builder(auto_ford)
    director.construct_auto()
    auto = director.get_auto()
    print(auto)
