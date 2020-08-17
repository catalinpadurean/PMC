# Imported modules

import os
import sys
import time

# print(os.path.exists("files/vegetables.txt"))
# print(os.path.exists("files/test_file.txt"))

while True:
    if os.path.exists("files/test_file.txt"):
        with open("files/test_file.txt") as file:
            print(file.read())
    else:
        print("File does not exist")
    time.sleep(10)
