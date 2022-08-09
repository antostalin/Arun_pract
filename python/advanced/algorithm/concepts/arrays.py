import sys


# Array memory allocation
def getsizeOf(n):
    data = []
    for x in range(n + 1):
        a = len(data)
        b = sys.getsizeof(data)
        print("Length: {0:3d}  size: {1:4d}".format(a, b))
        data.append(x)


# Array Fair Sum input -> ([1, 3, 2, 2], 4) output -> (1, 3), (2, 2)
def pair_sum(values, k):
    if len(values) < 2:
        return print("Too small value to process")

    seen = set()
    output = set()
    for num in values:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print("\n".join(map(str, list(output))))


# take an array with positive and negative integer and find the maximum sum of that array
def maxsum(arr):
    if len(arr) == 0:
        return print("Too small")

    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


# consider 2 array which has no duplicate and the second array can be start at any index
# if no two arrays are same means false
def rotate(list1, list2):
    if len(list1) != len(list2):
        return False

    key = list1[0]
    key_index = 0

    # find the starting index from list2
    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break

    if key_index == 0:
        return False

    for x in range(len(list1)):
        ls2index = (key_index + x) % len(list1)
        if list1[x] != list2[ls2index]:
            return False
    return True


# return the common elements from two array(consider it is already ascending order)
# input -> [1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10] output -> [1, 4, 9]
def common_elem(a, b):
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1])
            p1 += 1
            p2 += 1  # p2 += 2
        elif a[p1] > b[p2]:
            p2 += 1
        else:
            p1 += 1
    return result


# find the most occurrence item from the array
def most_frequent(arr):
    count = {}
    max_count = 0;
    max_item = None

    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    return max_item, max_count


if __name__ == '__main__':
    getsizeOf(10)

    print("\nArray Fair Sum:")
    pair_sum([1, 3, 2, 2], 4)

    print("\nFind maximum sum:", maxsum([2, 5, -1, 8, 12, 9, -3, 25, -16, 2]))

    print("\nRotation of Array:", rotate([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 1, 2, 3]))
    print("Rotation of Array:", rotate([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 8, 1, 2, 3]))
    print("Rotation of Array:", rotate([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 3, 2, 1]))

    print("\nCommon element:", common_elem([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]))

    (max_item, max_count) = most_frequent([1, 3, 3, 2, 1, 1, 1])
    print("\n{} item was found {} times".format(max_item, max_count))
