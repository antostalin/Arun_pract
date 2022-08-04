
class Voting:
    # this is a private method and cannot access outside the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__eligiblity = self.age >= 18  # private attribute

    def display(self):
        if self.__eligiblity:
            print("{} has eligibility for voting".format(self.name))
        else:
            print("{} has no eligibility for voting".format(self.name))

    # private attribute can be accessed by getter/setter method
    def get_elgibility(self):
        return self.__eligiblity


if __name__ == '__main__':
    arun = Voting('Arun', 12)
    antostalin = Voting('Antostalin', 25)
    arun.display()
    antostalin.display()
    print("Antostalin has voting eligibility:{}".format(antostalin.get_elgibility()))