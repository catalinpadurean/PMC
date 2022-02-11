#Linkuri utile
# 0. https://realpython.com/defining-your-own-python-function/
# 1. https://www.w3schools.com/python/python_functions.asp

# Define function print_hello_world()
# def print_hello_world():
#     print("Hello world from function!")

# print_hello_world()

# Call function print_hello_world()
# print_hello_world()
#
# Define function greet_by_name(name)
# def greet_by_name(name):
#     print(type(name))
#     print(f"Hello, {name}")
#
# def greet_by_name_age(surname, age=12, name="John"):
#     if age == 12:
#         print(surname)
#     else:
#         print(name)

# Call function greet_by_name(name) passing "John" as name
# greet_by_name_age(surname="smith", age=12, name= "A")
# greet_by_name_age("B", age=13, name="X" )
# greet_by_name_age("A", 13, "B" )
# greet_by_name_age("C", 10)
# greet_by_name_age("D")

#
#
# Define function greet_by_name(name) with default argument value
def greet_by_name(name="John"):
    if type(name) is str:
        print(f"Hello, {name}")
        print(f"Hello, {name.lower()}")
    else:
        print(f"the parameter is {type(name)}")

greet_by_name(5)
greet_by_name()
#
# Call function greet_by_name(name) using default value of the argument
# greet_by_name()  # prints 'Hello, World!'
# # # Call function greet_by_name(name) passing "John" as name
# greet_by_name("Ana")  # prints 'Hello, Ana'
# greet_by_name(name="John")  # prints 'Hello, John'

# Define function calculating volume of the cube
# def calculate_volume_of_the_cube(wall_length):
#     return wall_length ** 3

# volume = calculate_volume_of_the_cube(6)
# print(volume)  # prints 216

# Extra examples
# def greet_by_name2(a,b, name="Todd", name2="Chris" ):
#     print(f"hello {a}, {b} and good bye {name}, {name2}")
# #
# # greet_by_name2("Ana","John")
# #
# def greet_by_name3(a, b, d, e ,f, g, name="John",):
#     print(f"hello{a}, {b} and good bye {name},{d}, {e},{f}, {g}")
# # greet_by_name3("Ana","John","Tood", "Chirs", "Tony", "Luke", "Lola")
#
# def greet_by_name4(a = 5, b = "Ana", c = "John", d = "Carlos", e = "Carla" ,f = "Marry", g = 20):
#    print(f"These are some parameters {a}, {b} but so are these {c},{d}, {e},{f}, {g}")
# greet_by_name4(b = "param1", a = "param 2", c = "param 5", e = "param_4")
#
# def greet_by_name5(param_1, param_2):
#    print(f"These are some parameters {param_1}, {param_2} ")
# greet_by_name5("John", "Marry")
# greet_by_name5("John", "Marry")

"""Default empty list as optional argument example"""
# def f(my_list=[]):
#     my_list.append('###')
#     return my_list
#
# print(f())
# print(f())
# print(f())



""" In Python, default parameter values are defined only once when the function is defined (that is, when the def statement is executed).
 The default value isn’t re-defined each time the function is called. 
 Thus, each time you call f() without a parameter, you’re performing .append() on the same list. """

""" Handling for None argument"""
# def f(my_list=None):
#      if my_list is None:
#         my_list = []
#         #my_list.append('###') - decomentati aceasta linie dupa ce rulati codul cu ea comentata si observati diferentele
#      else:
#          my_list.append('###')
#      return my_list
#
# print(f())
# print(f([1,2]))
# print(f())
# print(f([3,4]))