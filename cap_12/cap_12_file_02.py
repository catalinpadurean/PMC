# Imported modules

import os
import pandas
import sys
import time

condition = True
timer = 1
while condition:
    print("Time is: {}".format(timer))
    if timer < 5:
        if os.path.exists("files/temps-today.csv"):
            data = pandas.read_csv("files/temps-today.csv")
            print("Data frame format for pandas is:")
            print(data)
            print("--------------------------------------------------------------------")
            print("Below is mean for all columns")
            print(data.mean())
            print("Below is mean for st1 column:")
            print(data.mean()["st1"])
            print("Below is mean for st2 column:")
            print(data.mean()["st2"])
        else:
            print("File does not exist. Will be created...")
            with open("files/temps-today.csv", "a+") as my_file:
                condition = False
                pass
    else:
        print("Time has run out. Must exit...")
        condition = False
    time.sleep(timer)
    timer = timer +1

#######################################################################################################################

# In this section you learned that:  Builtin objects are all objects that are written inside the Python interpreter in C language.

# Builtin modules contain builtins objects.

# Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

import time
time.sleep(5)
# A list of all builtin modules can be printed out with:

# import sys
sys.builtin_module_names
# Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

# Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

# Packages are a collection of .py modules.

# Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

# Third-party libraries can be installed from the terminal/command line:

# Windows: pip install pandas

# Mac and Linux: pip3 install pandas
