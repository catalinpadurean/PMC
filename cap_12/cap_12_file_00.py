# Imported modules
import sys
import time
sys.builtin_module_names
# print(sys.builtin_module_names)

timer = 1
while timer < 5:
    with open("files/vegetables.txt", "a+") as my_file:
        my_file.write("Time is: {}\n".format(timer))
        time.sleep(timer)
        if timer < 5:
            timer = timer + 1
        else:
            break;
