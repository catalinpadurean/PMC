# Linkuri utile

# 0. https://realpython.com/python-lists-tuples/
# Pentru aprofundare 'packing' si 'unpacking' link 1
# 1. https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

# Defining and Using Tuples
# Tuples are identical to lists in all respects, except for the following properties:
#
# Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
# Tuples are immutable.

# Declare and initialize a tuple
my_things = ("Dog", "Cat", 1997, 32.0, True)
# print(my_things)
my_things = "a", "b", "c", "d", 4
# print(my_things)
# print(type(my_things))
# my_things = ()
# print(type(my_things))
# Access tuple element and slice the tuple
my_things = ("Dog", "Cat", 1997, 32.0, True)
# print(my_things[0])
# print(my_things[1:3])
# my_things[0] = "A"

# Defining a tuple with one element
# tuple_1 = (4)
# print(type(tuple_1))
# tuple_2 = (4.5)
# print(type(tuple_2))
# tuple_3 = ('a')
# print(type(tuple_3))
# tuple_4 = (True)
# print(type(tuple_4))
#
# print("This happens because paranthesis are also used operators precedence in Python. \nSo, in order to have a tuple with one element we must include a comma after that element. See below")
# tuple_1 = (4, )
# print(type(tuple_1))
# tuple_2 = (4.5, )
# print(type(tuple_2))
# tuple_3 = ('a', )
# print(type(tuple_3))
# tuple_4 = (True, )
# print(type(tuple_4))

# Tuple packing and unpacking
#
tup = (1, 3.4, "S", True, None)
print(tup)
(t1, t2, t3, t4, t5) = tup
print(f"t1: {t1}")
print(f"t2: {t2}")
print(f"t3: {t3}")
print(f"t4: {t4}")
print(f"t5: {t5}")
print("="*40)
print(f"Type of t1: {type(t1)}")
print(f"Type of t2: {type(t2)}")
print(f"Type of t3: {type(t3)}")
print(f"Type of t4: {type(t4)}")
print(f"Type of t5: {type(t5)}")
print("="*40)
t1 = 12
print(tup)
print(len(tup))