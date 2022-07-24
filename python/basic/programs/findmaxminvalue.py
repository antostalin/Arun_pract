# find the max values by brut-force or iterative approach
def findmax(values):
    maxvalue = values[0]
    for x in values:
        # if x values is greater than maxvalue then set the max value to x
        if x > maxvalue:
            maxvalue = x
    return maxvalue


# find the max values by brut-force or iterative approach
def findmin(values):
    minvalue = values[0]
    for x in values:
        # if x values is smaller than minvalue then set the min value to x
        if minvalue > x:
            minvalue = x
    return minvalue


if __name__ == '__main__':
    lists = [15, 8, 25, 46, 3, 12, 37, 5]
    print("Printing the list values: ", lists)
    maxvalue = findmax(lists)
    minvalue = findmin(lists)
    print('Max:', maxvalue, ' Min:', minvalue)
