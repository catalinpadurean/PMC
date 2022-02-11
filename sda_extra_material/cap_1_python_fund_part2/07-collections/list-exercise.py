my_list = [1, 2, 3, 4, 5]

# a. Use len() to print its length.
print(len(my_list))

# b. Use append() to append a sixth element: another 2.
my_list.append(2)
print(my_list)

# c. Use count() to count the 2s in list.
print(my_list.count(2))

# d. Use the same function to count 7s, which are not in the list. What’s the result?
print(my_list.count(7))

# e. Use extend() to extend it with: [6, 7, 8].
my_list.extend([6, 7, 8])
print(my_list)

# f. Use index() to check index of the 7. Use indexing to check you got the correct result.
print(my_list.index(7))
print(my_list[7])

# g. Use insert() to add a value 10 at index 0. Print the list to check what it did.
my_list.insert(0, 10)
print(my_list)

# h. Use [-1] indexing to check the value of the last element.
print(my_list[-1])

# i. Use pop() to check the value of the last element, removing it from the list.
print(my_list.pop())

# j. Use remove() to delete 4 from the list.
my_list.remove(4)
print(my_list)

# k. Use reverse() and print the list..
my_list.reverse()
print(my_list)

# l. Use sort() and print it again.
my_list.sort()
print(my_list)

# m. Use clear() to empty the list.
my_list.clear()
print(my_list)
