# File processing

my_file = open("fruits.txt")
print(my_file.read())
print(my_file.read())  # the second read will print out an empty line because after the first read the cursor is at the EOF
print("-------------------------------------------------------------------------------------------------------------")
my_file2 = open("fruits.txt")
content = my_file2.read()
my_file2.close()

print(content) # saving the read method intro a variable and printing the variable will print each time to content of the file
print(content)


def foo(character, filepath = "fruits.txt"):
    file = open(filepath)
    f_content = file.read()
    return f_content.count(character)


print(foo("a"))
print("-------------------------------------------------------------------------------------------------------------")

with open("fruits.txt") as my_file3:  # with context manager will close the file automatically
    cont = my_file3.read()
print(cont)

print("-------------------------------------------------------------------------------------------------------------")

with open("files/vegetables.txt") as my_file4:
    my_content = my_file4.read()
print(my_content)
print("-------------------------------------------------------------------------------------------------------------")

with open("files/clothes", "w") as my_file5:  # if the file already exists Python will overwrite
    my_file5.write("Blouse\nPants\nSocks\n")
    my_file5.write("T-shirt")

with open("files/vegetables.txt", "a+") as file:
    file.write("\nOkra")
    file.seek(0)
    contenting = file.read()
print(contenting)


#######################################################################################################################

# In this section you learned that: You can read an existing file with Python:

with open("file.txt") as file:
    content = file.read()
# You can create a new file with Python and write some text on it:

with open("file.txt", "w") as file:
    content = file.write("Sample text")
# You can append text to an existing file without overwriting it:

with open("file.txt", "a") as file:
    content = file.write("More sample text")
# You can both append and read a file with:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
