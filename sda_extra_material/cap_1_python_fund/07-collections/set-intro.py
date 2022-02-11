# Linkuri utile
# 0. https://realpython.com/python-sets/
# 1. https://www.w3schools.com/python/python_sets.asp

# Python’s built-in set type has the following characteristics:
#
# Sets are unordered.
# Set elements are unique. Duplicate elements are not allowed.
# A set itself may be modified, but the elements contained in the set must be of an immutable type.


# Declare and initialize a set
animals = {"Dog", "Cat", "Elephant"}
animals_2 = set(["Mouse", "Rat", "Dolphin"])

# print(animals)
# print(type(animals))
# print(animals_2)
# print(type(animals_2))

# Differences between declaring a set with set functions and {}
# Diff1
# set_1 = set("football")
# print(f"Set_1: {set_1}")
# print(len(set_1))
# # Sets are unordered.!!!!!!!!!!!!!!!!!!!!!
# print(type(set_1))
# set_2 = {"football", "f","o", "otball"}
# print(f"Set 2: {set_2}")
# print(len(set_2))
# print(type(set_2))

# Diff2
x = ()
y = {}
#
print(x)
print(type(x))
print(y)
print(type(y))

print(help(set))



# Add an element
animals.add("Mouse")

# Add multiple elements
animals.update(["Bird", "Horse"])

# Declare and initialize a set
animals = {"Dog", "Cat", "Elephant"}

# Remove an element, throw an error if not present
animals.remove("Cat")

# Remove an element, DO NOT throw an error if not present
animals.discard("Cat")

# Other set methods

# print(help(set))
# print(animals)
# print(animals_2)
# print(animals.difference(animals_2))
# print(animals.union(animals_2))
# print(animals.intersection(animals_2))
