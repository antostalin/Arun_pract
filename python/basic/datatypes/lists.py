# List is ordered, mutable and allow duplicates
# Declare the list with empty, values and different datatype
list1 = []
list2 = [1, 2, 3, 4, 5]
list3 = ['Arun', 39, True]
print(list1)
print(list2)
print(list3)

# Different ways access the element from the list
print("\nValues in list2")
print("*********************************")
for x in list2:
    print(x)

print("\nValues in list3")
print("*********************************")
for index, x in enumerate(list3):
    print(index, " --> ", x)

print("\nAccess the elements in a list")
print("*********************************")
print(list2[2])
print(list3[:1])
print(list2[2:])  # Using split operator
print(list2[::1])  # Using step operator (using step1)
print(list2[::-1])  # Using reverse the list with step1
print(list2[::2])  # Access the element with step 2

# Some useful methods in list
print("\nVerifying some useful methods:")
print("*********************************")
fruits = ["Apple", "Orange", "Grapes", "Pineapple", "Custard Apple", "Papaya"]
print("fruits: ", fruits)

# in used for check the element present in the list
if "Apple" in fruits:
    print("Apple was found")
else:
    print("Apple was not found")

if "banana" in fruits:
    print("Banana was found")
else:
    print("Banana was not found")

# len() used to find the size of list
print("length of fruits: ", len(fruits))

# append() used to add the element at the last
fruits.append("Banana")
fruits.append("Guava")
print("After append the fruits: ", fruits)

# pop() will remove the last element from the list
print("Remove element using pop() :", fruits.pop())
print("Remove element using pop() :", fruits.pop())

# remove() will remove the specific element from the list
print("\nBefore remove: ", fruits)
fruits.remove("Papaya")
print("After remove Papaya:", fruits)
fruits.remove("Pineapple")
print("After remove Pineapple:", fruits)

# insert() used to insert a element to specific location
print("\nBefore insert: ", fruits)
fruits.insert(1, "Banana")
print("After insert Banana to 1 position: ", fruits)

# sort() -> sort the element from the list
# reverse() -> reverse the element from the list(alphabetical or numbers)
# clear() -> clear all element from the list
print("\nBefore sort: ", fruits)
fruits.sort()
print("After sort: ", fruits)
print("Before reverse: ", fruits)
fruits.reverse();
print("After reverse: ", fruits)
print("Before clear: ", fruits)
fruits.clear()
print("After clear: ", fruits)

# create a new list using some technique
numlist = [8, 2, 3, 9, 5]
print("\nCreating new list techniques")
print("Actual list: ", numlist)

# Assignment operator point to existing list reference so, modify the list will affect the original list
newlist = numlist
newlist.append(6)
newlist.append(7)
print("After assignment to new list: \n\tnewlist --> ", newlist, " \n\toriginal list --> ", numlist)

# sorted() will sort the element and create the new array
sortlist = sorted(newlist)
print("\nSorted list: ", sortlist, "\noriginal list --> ", numlist)
newlist = [2]*5
print("Create list using *: ", numlist)
newlist = numlist + [12, 15, 4, 5] # Using + operator to concat two list
print("\nBefore concatenation: ", numlist)
print("After concatenation: ", newlist)

# Some useful techniques of copy the list
print("\nCopying list techniques")
numlist = [1, 2, 3, 4, 5]
list1 = list.copy(numlist)
list2 = list(numlist)
list3 = []
list3[:] = numlist
print("\tOriginal list: ", numlist)
print("\tCopy using copy(): ", list1)
print("\tCopy using list(): ", list2)
print("\tCopy using [:]: ", list3)

# modify the element in original list
numlist.append(6)
numlist.append(7)
print("\nAfter updating the original list:")
print("\tOriginal list: ", numlist)
print("\tCopy using copy(): ", list1)
print("\tCopy using list(): ", list2)
print("\tCopy using [:]: ", list3)

# Other elegant way of copying the list
print("\nOther elegant way of copy of list")
# multiply with the same number
newlist = [x*x for x in numlist]
print("\tOriginal list: ", numlist)
print("\tNew list: ", newlist)

fruits = ["Apple", "Orange", "Grapes", "Pineapple"]
# working with string concatenation
newlist = [x+" fruit" for x in fruits]
print("\tOriginal list: ", fruits)
print("\tNew list: ", newlist)
