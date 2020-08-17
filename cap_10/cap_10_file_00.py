# More on functions


def area(a, b):
    return a * b


print(area(4, 5))  # non keyword arguments(positional arguments) because the first param(4) goes to a and the second(5) goes to b
print(area(a=6, b=7))  # keyword arguments because the position does not matter due to the fact that we specify each parameter where to be asigned
print(area(b=6, a=5))  # keyword arguments


def area2(a, b=8):
    return a*b


print(area2(9))  # default parameter b=8
print(area2(8, 98)) # default parameter can be overwritten


def mean(*args):
    return sum(args)/len(args)


print(mean(91, 2, 7))


def foo(*args):
    my_list = []
    for strong in args:
        my_list.append(strong.upper())
    return sorted(my_list)


def foo2(*args):
    return sorted(str.upper() for str in args)


print(foo("snow", "lava", "glacier", "water", "air"))
print(foo2("snow", "lava", "glacier", "water", "air"))


def foo3(**kwargs):  # unlimited keyword arguments **kwargs
    return kwargs    # will return a dictionary with keys beeing the name of the variables passed and values as values passed


print(foo3(a=1, b=22, c=33))


#######################################################################################################################

# In this section you learned that: Functions can have more than one parameter:


def volume(a, b, c):
    return a * b * c


# Functions can have default parameters(e.g.coefficient):


def converter(feet, coefficient=3.2808):
    meters = feet / coefficient
    return meters


print(converter(10))
# Output: 3.0480370641306997

# Arguments can be passed as non - keyword(positional) arguments(e.g.a) or keyword arguments(e.g.b = 2 and c = 10):


def volume(a, b, c):
    return a * b * c


print(volume(1, b=2, c=10))
# An * args  parameter allows the function to be called with an arbitrary number of non-keyword arguments:


def find_max(*args):
    return max(args)


print(find_max(3, 99, 1001, 2, 8))
# Output: 1001

# An ** kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:


def find_winner(**kwargs):
    return max(kwargs)


print(find_winner(Andy=17, Marry=19, Sim=45, Kae=34))
# Output: Sim





