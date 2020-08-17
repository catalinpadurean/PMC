# List comprehension

temps = [ 221, 234, 340, -999, 230]
new_temps = []

# loop
for temperature in temps:
    new_temps.append(temperature/10)

# list comprehension
new_temps2 = [temp/10 for temp in temps]

print("Loop:", new_temps)
print("Comprehension: ", new_temps2)

new_temps3 = [temp/10 for temp in temps if temp > 0]
print("Comprehension + IF conditional: ", new_temps3)

# if the conditional is IF-ELSE the FOR loop must be after the conditional
new_temps4 = [temp/10 if temp > 0 else 0 for temp in temps]
print("Comprehension + IF-ELSE conditional: ", new_temps4)

########################################################################################################################

# In this section you learned that:

# A list comprehension is an expression that creates a list by iterating over another container.

# A basic list comprehension:s

[i*2 for i in [1, 5, 10]]
# Output: [2, 10, 20]

# List comprehension with if condition:

[i*2 for i in [1, -2, 10] if i>0]
# Output: [2, 20]

# List comprehension with an if and else condition:

[i*2 if i>0 else 0 for i in [1, -2, 10]]
# Output: [2, 0, 20]
