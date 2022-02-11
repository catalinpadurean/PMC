#Linkuri utile:

# 0. https://realpython.com/python-lists-tuples/

# Declare and initialize a list variable
# alphabet = []  # this is an empty list
# print(f"Current length of 'alphabet': {len(alphabet)}")
#
# # Add some letters
# alphabet.append("a")
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.append("b")
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.append("c")
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.append(24)
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.append(True)
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.append([True, False, True, 4.89])
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.extend([True, False, True, 4.89])
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.append([3, 4])
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.append("3,4")
# print(f"Alphabet: {alphabet} (length: {len(alphabet)})")
# alphabet.sort()
# print(f"Alphabet (sorted): {alphabet} (length: {len(alphabet)})")


# Indexing
# print(f"The first letter of alphabet is '{alphabet[0]}'")
#
# # # Add some more letters
# alphabet.extend(["f", "d", "g", "e"])
# print(f"Alphabet (mixed): {alphabet} (length: {len(alphabet)})")

# # Diff between append and extend
# alphabet_temp = ["a", "b", "c", 1, 5.4, True]
# print(f"Alphabet-temp: {alphabet_temp} (length: {len(alphabet_temp)})")
# alphabet_temp.append(["f", "d", "g", "e"])
# print(f"Alphabet-temp: {alphabet_temp} (length: {len(alphabet_temp)})")
# print(alphabet_temp)

# Sort the list
# alphabet.sort()
# print(f"Alphabet (sorted): {alphabet} (length: {len(alphabet)})")


# The important characteristics of Python lists are as follows:
#
# Lists are ordered.
# list_1 = ['foo', 'bar', 'baz', 'qux']
# list_2 = ['foo', 'qux', 'bar', 'foo']
# print(list_1[0:2] == list_2[0:2])

# Lists can contain any arbitrary objects.
# list_1 = ['foo', 'bar', 'baz', 'qux']
# list_2 = ['baz', 'qux', 1, 2.534, True, "╬6"]
# list_3 = [int, len, str, chr, ord]  # even functions
# list_4 = [1, 2, "abcde", len, [1, 45, "ABCDE", max]]
# print(list_1)
# print(list_2)
# print(list_3)
# print(list_4)

# # List elements can be accessed by index.
# print(list_2[3])
# #Virtually everything about string indexing works similarly for lists.
# #For example, a negative list index counts from the end of the list:
# print(list_1[::])
# print(list_1[::-1])
# print(list_1[-3:-1])
# print(list_1[1:3])

# Lists are mutable.

# list_5 = ['foo', 'bar', 'baz', 'qux']
# print(list_5)
# list_5[2] = 30
# print(list_5)
# list_5.insert(2, 45)
# print(list_5)
# list_5[2] = 70
# print(list_5)
# list_5.insert(45, 2)
# list_5.insert(34, 10)
# list_5.insert(2, 11)
# print(list_5)
# print(len(list_5))
# # print(list_5[45])
# list_5[-2] ="aaaaa"
# print(list_5)
# print(list_5[1:3])
# list_5[2:4] = [1, 2, 3, 4, 5, 7, 8]
# print(list_5)
# list_5 = list_5 + [2, 4, 6, 8]
# print(list_5)
# list_5 = [1, 3, 5, 7] + list_5
# print(list_5)

# Lists are dynamic.
# Every example shown above demonstrates that a list will expand and adapt in each direction as the user requests it
