recipe = ("boil water", "insert egg", "wait 5min", "eat")

# a. Use len() to print out its length.
print(len(recipe))

# b. Use get-item operator [], to get 3rd step of the recipe.
print(recipe[2])

# c. Print out a slice of the last two steps of the recipe.
print(recipe[len(recipe) - 2:])

# d. Count occurrences of “wait 5min” using count() function.
print(recipe.count("wait 5min"))

# e. Check whether “boil water” is the first step using index() function.
print(recipe.index("boil water"))

print(help(tuple))