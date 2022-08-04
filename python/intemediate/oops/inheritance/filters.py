class Filter:
    def init(self):
        self.blocked = []

    def filter(self, values):
        return [x for x in values if x not in self.blocked]


class NullFilter(Filter):
    def init(self):
        self.blocked = ['null']


class ZeroFilter(Filter):
    def init(self):
        self.blocked = [0, -5]


if __name__ == '__main__':
    # create the object of base class
    flr = Filter()
    flr.init()
    print("\nWithout any Filter:")
    print(flr.filter([1, 2, 3, 4]))

    nullflr = NullFilter()
    nullflr.init()
    print("\nNull Filter:")
    print(nullflr.filter(['hello', 'null', 'null', 'egg', 'null', 'chicken']))

    zeroflr = ZeroFilter()
    zeroflr.init()
    print("\nZero Filter:")
    print(zeroflr.filter([3, 8, 0, 2, 7, -5, 0, 5]))

    print("\nValidating the inheritance")
    print("ZeroFilter is subclass of Filter:", issubclass(ZeroFilter, Filter))
    print("Filter is subclass of NullFilter:", issubclass(Filter, NullFilter))
    print("NullFilter baseclass:", NullFilter.__base__)
    print("Filter baseclass:", Filter.__base__)
    print("zeroflr instance of ZeroFilter:", isinstance(zeroflr, ZeroFilter))
    print("zeroflr instance of Filter:", isinstance(zeroflr, Filter))
    print("zeroflr instance of String:", isinstance(zeroflr, str))
    print("nullflr is a type:", nullflr.__class__)
