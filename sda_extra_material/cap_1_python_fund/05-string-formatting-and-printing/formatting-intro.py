# Formatting and printing (old style)
name = "General"
last_name = "Kenobi"
print("-"*50)
print("This is old style printing")
print("Hello there, %s %s %s" % (last_name, name, 2))
print("Hello there, %(name_)s %(last_name)s" % {"name_": name, "last_name": last_name})
print("-"*50)
#
# Formatting and printing (new style)
name_var = "General"
last_name_var = "Kenobi"
print("This is new style printing")
greetings = "Hi, there, {}{}"
print("!!!! Hello there, {} {}".format(last_name, name))
print(greetings.format(name, last_name))
print("Hello there, {name_par} {last_name_par}".format(last_name_par=last_name_var, name_par=name_var,))
print("-"*50)

# Formatting and printing (string interpolation)
# name = "General"
# last_name = "Kenobi"
# print("This is string interpolation style printing")
# print(f"Hello there, {name} {last_name}")
# a = 2
# b = 7
# print(f"{a} times {b} raised to power of 2 is {(a * b) ** 2}.")

# Changing how variable is displayed
header1 = "Name"
header2 = "Age"
name = "John"
age = 22

print(f"| {header1.center(10,'O'):10} | {header2:10} |")

print("-" * 27)
print(f"| {name:10} | {age:10} |")

n = 109.432148881111
print(f"{n:.4f}")  # prints out 109.432
print(f"{n:.1f}")  # prints out 109.4
print(f"{n:.7f}")  # prints out 109.4321889

voters_percentage = 0.71
print(f"{voters_percentage:.1%}")  # prints out 71.0%
print(f"{voters_percentage:.3%}")  # prints out 71.000%
voters_percentage = (0.71 * 2.24569)
print(f"{voters_percentage:.2%}")  # prints out ...