# Python basics: functions and conditionals


def foo(x, array):
    if x in array:
        return True
    else:
        return False


print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))


# Use isinstace for getting the data type of one variable

def get_type(target_variable):
    if isinstance(target_variable, dict):
        print("Target variable is a dictionary")
    elif isinstance(target_variable, list):
        print("Target variable is a list")
    elif isinstance(target_variable, int):
        print("Target variable is an integer")
    else:
        print("Target variable is not a recognized type or class inside of this function")


get_type([2, 34])
get_type(2.4)
get_type("abcdedgf")
get_type({"Mary": 23, "Jon": 69})
get_type(200000)


########################################################################################################################

# In this section you learned to:

#Define a function:


def cube_volume(a):
    return a * a * a


#Write a conditional block:

message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")
# Write a conditional block of multiple conditions:

message = "hello there"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
# Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")
# Output is Yes since both x and y are 1.

# Use the or operator to check if at least one condition is True:

x = 1
y = 2

if x == 1 or y == 2:
    print("Yes")
else:
    print("No")
# Output is Yes since x is 1.

# Check if a value is of a certain type with:
isinstance("abc", str)
isinstance([1, 2, 3], list) or type("abc") == str
type([1, 2, 3]) == list
