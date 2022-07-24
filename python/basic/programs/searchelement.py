# If search a element then we need source and which element to be searched from the source
# So, this function should expect 2 params like source and search element
def searchfound(lists, searchvalue):
    # brut-force or iterative approach
    isfound = False
    for x in lists:
        if x == searchvalue:
            isfound = True
    return isfound


# The parameters are same like above
def searchindex(lists, searchvalue):
    # brut-force or iterative approach
    for index, x in enumerate(lists):
        if x == searchvalue:
            # index will start from 0 so, adding 1 to the index
            return index+1
    return -1


def searchstatus(lists, searchvalue):
    print("Searching ", searchvalue, " from the list")
    isfound = searchfound(lists, searchvalue)
    if isfound:
        index = searchindex(lists, searchvalue)
        print(searchvalue, " found at ", index, " position")
    else:
        print(searchvalue, " was not found")


if __name__ == '__main__':
    lists = [15, 8, 25, 46, 3, 12, 37, 5]
    print("Printing the list values: ", lists)
    searchstatus(lists, 12)
    searchstatus(lists, -5)
    searchstatus(lists, 5)
    searchstatus(lists, 10)
