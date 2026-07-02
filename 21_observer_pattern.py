
class Observer:
    def update(self, msg):
        pass

    def finish(self):
        pass

class EventBus:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def unregister_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

    def finish_for_all(self):
        for obs in self.observers:
            obs.finish()

class Printer(Observer):
        def update(self,msg):
            print(msg)

class ToFile(Observer):
        def __init__(self):
            self.f = open("logs_01.txt", "w", encoding="utf-8")

        def update(self,msg):
            self.f.write(msg)
            self.f.write("\n")

        def finish(self):
            self.f.close()



bus = EventBus()
p1 = Printer()
file_writer = ToFile()
bus.register_observer(p1)
bus.register_observer(file_writer)

while True:
    var1 = input("Message:\n")

    if var1 == "exit":
        print("Ending program")
        break

    bus.notify(var1)

bus.finish_for_all()