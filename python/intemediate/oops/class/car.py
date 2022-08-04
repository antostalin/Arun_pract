class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("{} car was started".format(self.name))

    def move(self, speed):
        print("{} car was moved with {} speed".format(self.name, speed))

    def stop(self):
        print("{} car was stopped".format(self.name))

    def display(self):
        print("{} car in {} color".format(self.name, self.color))


def repair():
    print("Car was repaired. It should go to service station")


if __name__ == '__main__':
    audi = Car('Audi', 'Grey')
    bmw = Car('BMW', 'Black')

    audi.display()
    audi.start = audi.start  # define the self method as reference <class 'method'>
    print(type(audi.start))
    audi.start()
    audi.move(50)
    audi.stop()

    bmw.repair = repair  # define the method outside the class <class 'function'>
    print(type(bmw.repair))
    bmw.display()
    bmw.start()
    bmw.repair()

