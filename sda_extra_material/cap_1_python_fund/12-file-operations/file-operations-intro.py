# Linkuri utile
# 0. https://realpython.com/working-with-files-in-python/
# 1. https://realpython.com/read-write-files-python/
# 2. https://www.w3schools.com/python/python_file_handling.asp
# 3. https://realpython.com/python-enumerate/
# 4. https://www.guru99.com/reading-and-writing-files-in-python.html


# Enumerate is a built-in function in python
# When you use enumerate(), the function gives you back two loop variables:
# The count of the current iteration, in cazul nostru =>contor_linie
# The value of the item at the current iteration, in cazul nostru =>valoare_line
with open("data/example.txt", 'r') as f:  # f is a file object
    for contor_linie, valoare_linie in enumerate(f):  # iterate every line of the file
        # print(i, line)
        # print(line)
        if contor_linie == 0:  # skip first line
            continue
        clean_line = valoare_linie.rstrip()  # remove "\n" - end of line character at the end of each line
        if clean_line == "":  # skip empty lines
            continue
        print(clean_line)
# f.close() is called automatically when code exits "with open()" block


with open("data/sample_2.txt", "w+") as f:  # open file in write mode
    for i in range(1,3):
        f.write(f"This is line number {i}\n")  # write to file, adding new line with each iteration

# ● “r” - read mode (default),
# ● “w” - write mode,
# ● “x” - exclusive creation, fails if the file already exists,
# ● “a” - open for writing, appending to the end of file (if file exists),
# ● “b” - binary mode,
# ● “t” - text mode (default),
# ● “+” - open file for updating (reading and writing).

# with open ("data/sample.txt", "r") as file_1:  # open file in write mod
#     print(file_1.read().split("\n"))
#     print(type(file_1.read().split()))
#
# with open("data/sample.txt", "a") as f:  # open file in write mode
#     for i in range(11,15):
#         f.write(f"This is line number {i}\n")  # write to file, adding new line with each iteration

