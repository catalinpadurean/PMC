# Printing out multiple strings
print("What", "a", "lovely", "day", ".")
print("1", "2", 3, 4, 5)
fruit = "orange"
print("apple", "banana", fruit)

# Printing out multiple strings with a separator
print("What", "a", "lovely", "day", ".", sep="-")
print("1", "2", 3, 4, 5, sep=" < ")
fruit = "orange"
print("apple", "banana", fruit, sep=" + ")

# Printing out multiple strings with a separator and ending
print("What", "a", "lovely", "day", ".", sep="-", end="!\n")
print("1", "2", 3, 4, 5, sep=" < ", end=" < ...\n")
fruit = "orange"
print("apple", "banana", fruit, sep=" + ", end=" = yummy\n")
