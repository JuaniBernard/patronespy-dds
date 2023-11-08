from subject import Subject

class AlarmaLibro(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
