class ClassCounter:
    # class level attribute
    counter = 0

    def init(self):
        ClassCounter.counter += 1

    def display(self):
        print("Class has visited {} times".format(ClassCounter.counter))


if __name__ == '__main__':
    c1 = ClassCounter()
    c1.init()
    c1.display()
    c2 = ClassCounter()
    c2.init()
    c2.display()

    # alternate way of accessing the attribute
    print("C1 count:{}".format(c1.counter))
    print("C2 count:{}".format(c2.counter))

    c1.counter = 'Hello'
    print("\nAfter change the value to string")
    print("C1 count:{}".format(c1.counter))
    print("C2 count:{}".format(c2.counter))