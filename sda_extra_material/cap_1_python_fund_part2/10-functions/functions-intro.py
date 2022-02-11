# Define function print_hello_world()
def print_hello_world():
    print("Hello world from function!")


# Call function print_hello_world()
print_hello_world()


# Define function greet_by_name(name)
def greet_by_name(name):
    print(f"Hello, {name}")


# Call function greet_by_name(name) passing "John" as name
greet_by_name("John")


# Define function greet_by_name(name) with default argument value
def greet_by_name(name="World!"):
    print(f"Hello, {name}")


# Call function greet_by_name(name) using default value of the argument
greet_by_name()  # prints 'Hello, World!'
# Call function greet_by_name(name) passing "John" as name
greet_by_name("John")  # prints 'Hello, John'
greet_by_name(name="John")  # prints 'Hello, John'


# Define function calculating volume of the cube
def calculate_volume_of_the_cube(wall_length):
    return wall_length ** 3


volume = calculate_volume_of_the_cube(6)
print(volume)  # prints 216
