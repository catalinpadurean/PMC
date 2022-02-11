with open("data/example.txt") as f:  # f is a file object
    for i, line in enumerate(f):  # iterate every line of the file
        if i == 0:  # skip first line
            continue
        clean_line = line.rstrip()  # remove "\n" - end of line character at the end of each line
        if clean_line == "":  # skip empty lines
            continue
        print(clean_line)
# f.close() is called automatically when code exits "with open()" block


with open("data/sample.txt", "w+") as f:  # open file in write mode
    for i in range(10):
        f.write(f"This is line number {i}\n")  # write to file, adding new line with each iteration
