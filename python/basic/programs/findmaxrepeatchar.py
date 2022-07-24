# Split the string to each character then count the each character
# then we can take the max or min count of each char
def splitandcountchar(value):
    splitter = []
    splitter[:] = value
    # Dictionary will store the value as char:count e.g('a':1)
    charcount = {}

    for x in splitter:
        # simply ignore the space between the letters
        if x == " ":
            continue

        # Assume the entry is not found in dict means it's a new entry to be added
        if charcount.get(x) is None:
            charcount[x] = 1
        # If the entry already found then we need to increase the count
        else:
            charcount[x] = charcount.get(x) + 1
    return charcount


def findmaxrepeatchar(value):
    dict = splitandcountchar(value)
    # Initialize with first dict value
    keys = list(dict.keys())
    maxvalue = dict.get(keys[0])
    maxrepeatchar = ''

    # Same iteration itself we can save the max key otherwise it required additional iteration
    for key, value in dict.items():
        if maxvalue < value:
            maxvalue = value
            maxrepeatchar = key
        if maxvalue == value:
            maxrepeatchar = key
    return maxrepeatchar


def findminrepeatchar(value):
    dict = splitandcountchar(value)
    # Initialize with first dict value
    keys = list(dict.keys())
    minvalue = dict.get(keys[0])
    minrepeatchar = ''

    for key, value in dict.items():
        if minvalue > value:
            minvalue = value
            minrepeatchar = key
        if minvalue == value:
            minrepeatchar = key
    return minrepeatchar

# Something has to be improved
# use unpacking to return the min/max on the same function
# we can return list if the max or in has more than one element

if __name__ == "__main__":
    splitchar = "hello world"
    print("Actual String: ", splitchar)
    maxrepeatchar = findmaxrepeatchar(splitchar)
    minrepeatchar = findminrepeatchar(splitchar)
    print("Max Repeated Character: ", maxrepeatchar)
    print("Min Repeated Character: ", minrepeatchar)
