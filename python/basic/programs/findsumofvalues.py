def sumofvalue(lists):
    sum = 0
    for x in lists:
        sum += x
    return sum


if __name__ == '__main__':
    lists = [10, 3, 16, 5, 8, 7]
    print('List of values: ', lists)
    result = sumofvalue(lists)
    print("Sum= ", result)
