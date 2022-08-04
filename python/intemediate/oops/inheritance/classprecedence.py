
class Bird:
    def fly(self):
        print("Bird was flying")

    def walk(self):
        print("Bird was walking")


class Animal:
    def walk(self):
        print("Animal was walking")

    def run(self):
        print("Animal was running")

# Penguin is a bird but it won't fly and can walk or run.
# Suppose we want to deprecate the same method exists in both parent class;
# then, change the order of MRO(Method resolution order) of execution
class Penguin(Animal, Bird):
    pass


if __name__ == '__main__':
    penguin = Penguin()
    penguin.walk()  # walk() method in both Bird and Aninal class but based on order it give precedence to Animal class
    penguin.run()
