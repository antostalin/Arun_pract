#Big(O) notation
# o(log n), o(1) - excellent/good,
# o(n) - fair,
# o(n log n) - bad,
# o(n^2), o(2^n) o(n!) - horrible

# o(1) - constant
def func_test(values):
    return values[0]


# o(n) - linear
# if thiis function call 3 times then 3(n) which is similar to o(n)
def printlst(lst):
    for x in lst:
        print(str(x))


# o(n ^ 2) - quadratic
def quadraticlst(lst):
    for x in lst:
        for y in lst:
            print(x, ",", y)


# o(1+n/2+10) -- constant is not valid as varies n values, so o(n)
def comp(lst):
    print(lst[0])  # o(1)
    midpoint = len(lst) // 2
    for val in lst[:midpoint]:  # o(n/2)
        print(val)

    for x in range(10):  # o(10)
        print('number')


def matcher(lst, match):
    for x in lst:
        if x == match:
            return True
        else:
            return False


def memory(n):
    for x in range(n):  # Time Complexity o(n)
        print("Hello!!")  # Space Complexity o(1)


if __name__ == '__main__':
    print("o(1) -->", str(func_test([1, 2, 3, 4])))
    print("o(n) -->")
    printlst([1, 2, 3, 4, 5, 6])
    print("o(n ^ 2) -->")
    print(quadraticlst([1, 2, 3]))

    print(comp([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(matcher(lst, 1))  # o(1) best case scenarios
    print(matcher(lst, 20))  # o(n) worst case scenario

    # space and time complexity
    memory(10)
