# #Linkuri utile:
#
# # 0. https://realpython.com/python-dicts/
#
# # Declare and initialize an empty dictionary
# phonebook = {}
#
# # Add elements
# # phonebook["John"] = 111111111
# # phonebook["Jack"] = 222222222
#
# # print(phonebook)  # prints out {'John': 111111111, 'Jack': 222222222}
# # print(phonebook["Jack"])  # prints out 222222222
# #
# # Declare and initialize a dictionary
phonebook = {
    "John": [111111111, 5],
    "Jack": 222222222
}
# # print(phonebook)
# phonebook["John2"] = 1111111113
# phonebook["Jack2"] = 2222222224
# # print(phonebook)
#
# # print(phonebook)  # prints out {'John': 111111111, 'Jack': 222222222}
# # print(phonebook["Jack"])  # prints out 222222222
#
# # # Declare and initialize a dictionary
# # phonebook = {
# #     "John": 111111111,
# #     "Jack": 222222222
# # }
# #
# # # Delete elements
# # del phonebook["John"]
# # phonebook.pop("Jack")
# #
print(phonebook)
# #
# # # Declare and initialize a dictionary
# # phonebook = {
# #     "John": 111111111,
# #     "Jack": 222222222
# # }
# #
# # # Find element by key that does not exist
# # print(phonebook.get("Dory"))  # prints out None
# # print(phonebook.get("Dory", 0))
# # phonebook["John2"] = "0737-455-677"
# # print(phonebook)
# # # prints out 555555555 because 55555555 is the default value if the key is not found
# # print(help(dict))
#
# # print(phonebook)
# # print(phonebook.items())
# # list1 = phonebook.items()
# # print(type(list1))
# # list2 = list(phonebook.items())
# # print(type(list2))
# # print(list(phonebook.keys()))
# # print(phonebook.pop("John", "Not found"))
#
# # print(phonebook.popitem())
# phonebook.setdefault("Ana", "9999")
# # phonebook["Ana"] = 2
# # print(phonebook)
# # print(list(phonebook.values()))
# # print(phonebook)
# # new_pers = {"Ana" : 49, "Cristi" : 90}
# # phonebook.update(new_pers)
# print(phonebook)
# print(phonebook.setdefault("Ana", "xxx"))
# phonebook["Ana"] = "yyyy"
print(phonebook.get('John'))
print(phonebook['John'][0])

# print(help(dict))