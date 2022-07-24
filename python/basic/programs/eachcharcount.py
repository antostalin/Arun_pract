# Split the string to each character then count the each character
# then we can find the each char count in a string
def splitandcountchar(value):
    splitter = []
    splitter[:] = value
    #print(splitter)

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
    display(charcount)


def display(dict):
    for key, value in dict.items():
        # Ternary operator
        times = " times" if value > 1 else " time"
        print(key, " in ", value, times)


if __name__ == "__main__":
    splitchar = "hello world"
    print("Actual string:", splitchar)
    splitandcountchar(splitchar)
