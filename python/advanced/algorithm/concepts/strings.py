# the letters should frame another letter with same letter and count
def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) == len(s2):
        return sorted(s1) == sorted(s2)


# find the same logic with dict and count
def anagram_dict(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}
    # insert the letters with count
    for x in s1:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

    # remove the letter count from dict
    for x in s2:
        if x in count:
            count[x] -= 1
        else:
            count[x] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True


# reverse a string
def reverse1(s):
    return '-'.join(reversed(s.split()))


def reverse2(s):
    s = s.split()
    s.reverse()
    return s


def reverse3(s):
    return '-'.join(s.split()[::-1])


def reverse(s):
    length = len(s)
    spaces = [' ']
    i = 0
    words = []

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1

    return ' '.join(reversed(s))


# find the string has unique character
def unique1(s):
    s = s.replace(' ', '')
    return len(set(s)) == len(s)


def unique(s):
    s = s.replace(' ', '')
    character = set()

    for letter in s:
        if letter in character:
            return False
        else:
            character.add(letter)
    return True


# find the non-repeating char in a string
def non_repeating(s):
    s = s.replace(' ', '').lower()
    char_count = {}

    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    # this will return the first unique element
    for c in s:
        if char_count[c] == 1:
            return c

    return None


def find_allunique(s):
    s = s.replace(' ', '').lower()
    char_count = {}

    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    all_unique = []
    y = sorted(char_count.items(), key=lambda x: x[1])
    print(y)

    for item in y:
        if item[1] == y[0][1]:
            all_unique.append(item)

    return all_unique


if __name__ == '__main__':
    print("Anangran: dog and god: ", anagram('dog', 'god'))
    print("Anagram: clint eastwood and old west action: ", anagram('clint eastwood', 'old west action'))
    print("Anagram: aa and bb: ", anagram('aa', 'bb'))

    print("\nAnagram using dict and count")
    print("Anangran: dog and god: ", anagram_dict('dog', 'god'))
    print("Anagram: clint eastwood and old west action: ", anagram_dict('clint eastwood', 'old west action'))
    print("Anagram: aa and bb: ", anagram_dict('aa', 'bb'))

    s = 'This is the best'
    print("\nReverse a string: ", reverse1(s))
    print("Reverse as list: ", reverse2(s))
    print("Reverse as index: ", reverse3(s))
    print("Reverse as algo: ", reverse(s))

    print("\nString unique: ", unique1("a b cdef"))
    print("String unique algo: ", unique("a b cdef"))
    print("String unique algo: ", unique("a bb cdef"))

    print("\nNon-repeating character: ", non_repeating("I Apple Ate peel"))
    print("Non-repeating all character: ", find_allunique("I Apple Ate peel"))
