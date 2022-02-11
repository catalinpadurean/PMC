# Formatting and printing (old style)
name = "General"
last_name = "Kenobi"
print("Hello there, %s %s" % (name, last_name))
print("Hello there, %(name)s %(last_name)s" % {"name": name, "last_name": last_name})

# Formatting and printing (new style)
name = "General"
last_name = "Kenobi"
print("Hello there, {} {}".format(name, last_name))
print("Hello there, {name} {last_name}".format(name=name, last_name=last_name))

# Formatting and printing (string interpolation)
name = "General"
last_name = "Kenobi"
print(f"Hello there, {name} {last_name}")
a = 2
b = 7
print(f"{a} times {b} raised to power of 2 is {(a * b) ** 2}.")

# Changing how variable is displayed
header1 = "Name"
header2 = "Age"
name = "John"
age = 22

print(f"| {header1:10} | {header2:10} |")
print("-" * 27)
print(f"| {name:10} | {age:10} |")

n = 109.432188881111
print(f"{n:.3f}")  # prints out 109.432

voters_percentage = 0.71
print(f"{voters_percentage:.1%}")  # prints out 71.0%
