# Declare and initialize an empty dictionary
phonebook = {}

# Add elements
phonebook["John"] = 111111111
phonebook["Jack"] = 222222222

print(phonebook)  # prints out {'John': 111111111, 'Jack': 222222222}
print(phonebook["Jack"])  # prints out 222222222

# Declare and initialize a dictionary
phonebook = {
    "John": 111111111,
    "Jack": 222222222
}

print(phonebook)  # prints out {'John': 111111111, 'Jack': 222222222}
print(phonebook["Jack"])  # prints out 222222222

# Declare and initialize a dictionary
phonebook = {
    "John": 111111111,
    "Jack": 222222222
}

# Delete elements
del phonebook["John"]
phonebook.pop("Jack")

print(phonebook)

# Declare and initialize a dictionary
phonebook = {
    "John": 111111111,
    "Jack": 222222222
}

# Find element by key that does not exist
print(phonebook.get("Dory"))  # prints out None
print(phonebook.get("Dory", 555555555))  # prints out 555555555
