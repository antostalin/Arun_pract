from abc import ABC, abstractmethod

# abstract class can help to achieve 50% of abstraction i.e partially implementation
# done from base class and the remaining changes leave to the child classed but,
# still it required the dependency with base class implementation
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def move(self, speed):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car was started")

    def move(self, speed):
        print("Car was moving with {} speed".format(speed))

    def stop(self):
        print("Car was stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike was started")

    def move(self, speed):
        print("Bike was moving with {} speed".format(speed))

    def stop(self):
        print("Bike was stopped")

# we can register Bus class to the Vehicle class but we should make sure that,
# all expected methods are defined in the class
class Bus:
    def start(self):
        print("Bus was started")

    def stop(self):
        print("Bus was stopped")


if __name__ == '__main__':
    audi = Car()
    audi.start()
    audi.move(100)
    audi.stop()

    bullet = Bike()
    bullet.start()
    bullet.move(50)
    bullet.stop()

    print("\nAudi is a vehicle", isinstance(audi, Vehicle))
    print("Bullet is a vehicle", isinstance(bullet, Vehicle))
    print("Car is subclass of vehicle:", issubclass(Car, Vehicle))

    Vehicle.register(Bus)
    benz = Bus()
    print("\nBus is a vehicle", isinstance(benz, Vehicle))
    print("Bus is subclass of vehicle", issubclass(Bus, Vehicle))
    benz.start()
    benz.stop()