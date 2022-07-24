def printoddnum(values):
    print("Printing Odd number is: ")
    for x in values:
        if x % 2 == 1:
            print(x)


def printevennum(values):
    print("Printing Even number is:")
    for x in values:
        if x % 2 == 0:
            print(x)


if __name__ == '__main__':
    lists = [2, 5, 7, 10, 15, 12, 18, 21]
    # change this value to True to print the odd numbers
    isOdd = False
    print("List values: ", lists)
    if isOdd:
        printoddnum(lists)
    else:
        printevennum(lists)
