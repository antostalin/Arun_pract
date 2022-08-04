class Person:
    # define constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # define generators
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # define other methods
    def display(self):
        print("Hello {} your age is {}".format(self.name, self.age))


if __name__ == '__main__':
    # declare the class
    arun = Person('Arun', 39)
    antostalin = Person('Antostalin', 29)

    # call the class method to display the value
    arun.display()
    antostalin.display()

    # modify the value after object was created
    print("\nAfter modifying the values")
    arun.set_name('Geo Mathew')
    antostalin.set_age(35)

    # call the class method to display the value
    arun.display()
    antostalin.display()

    # alternate way of accessing the attribute or members of a class
    print("\nAlternate way of accessing the values")
    print(arun.name, ",", arun.age)
    print(antostalin.name, ",", antostalin.age)

    # display class type and attributes
    print("\nClass type and attributes")
    print(type(arun))
    print(arun.__class__.__name__)
    p = dir(arun)  # dir() will help to access the method through class object
    print(p)

