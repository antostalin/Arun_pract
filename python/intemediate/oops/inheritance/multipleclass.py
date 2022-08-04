
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi! the value is {}".format(self.value))


class TalkCalculator(Calculator, Talker):
    pass


if __name__ == '__main__':
    talkcal = TalkCalculator()
    talkcal.calculate('1 + 4 * 4')
    talkcal.talk()

    print("\nTalking calculator has talk method:", hasattr(talkcal, 'talk'))
    print("Talking calculator has nomethod:", hasattr(talkcal, 'nomethod'))
    print("talk() called:", callable(getattr(talkcal, 'talk', None)))
    print("nomethod() called:", callable(getattr(talkcal, 'nomethod', None)))
    setattr(talkcal, 'name', 'Arun Stephen')
    print("Name: ", talkcal.name)