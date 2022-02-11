#Linkuri utile:
# 0. https://docs.python.org/3/library/sys.html
# 1. https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/

# Import sys module and read command line parameters
import sys

# prints out full path to the application and its name
print(f"Application name: {sys.argv[0]}")
print(f"First argument: {sys.argv[1]}")  # prints out hello
# print(f"Second argument: {sys.argv[2]}")  # prints out world!

print(type(sys.argv))
variabila_python = "am primit " + sys.argv[1]
var_py = sys.argv
print(var_py)


# Try from terminal:
# -go to your current working directory (cd, cd.., dir,)
        # https://www.ionos.com/digitalguide/server/know-how/windows-cmd-commands/
# -execute command: pyhton.exe command-line-parameters-intro.py hello world
