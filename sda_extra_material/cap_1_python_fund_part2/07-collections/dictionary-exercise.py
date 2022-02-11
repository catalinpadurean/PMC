my_dictionary = {1: "one", 2: "two", 3: "three"}

# a. Use len() to print its length.
print(my_dictionary)

# b. Using set-item operator [], add a new key-pair: 4:"four".
my_dictionary[4] = "four"

# c. Using get-item operator [], print out the value assigned to key 2.
print(my_dictionary[2])

# d. Using get-item operator [], print out value for unassigned key, like 10. What happens?
# print(my_dictionary[10])

# e. Using dictionary function get(key), replace the previous get-item operator []
# and print out the value for key 10. What happens?
print(my_dictionary.get(10))

# f. Using dictionary function get(key, default), print out the value for key 10,
# this time setting default value to "unknown".
print(my_dictionary.get(10, "unknown"))

# g. Using dictionary function get(key, default), print out the value for key 3. Set default value to "unknown".
print(my_dictionary.get(3, "unknown"))

# h. Use pop() to print out value assigned to 2. Print out the dictionary after using pop().
print(my_dictionary.pop(2))
print(my_dictionary)

# i. Create a new dictionary {0: "zero"}. Using update(), update main dictionary with
# values from the new dictionary. Print out the main dictionary.
my_dictionary.update({0: "zero"})
print(my_dictionary)

# j. Using clear(), clear the dictionary.
my_dictionary.clear()
print(my_dictionary)
