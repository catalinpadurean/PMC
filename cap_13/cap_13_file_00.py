# No.1 application: Interactive dictionary

import json

data = json.load(open("files/data.json"))
print(type(data))
# print(data)
# print(data["rain"])

# check for word in dictionary and return the definition taking into account case sensitivity


def return_one_word(key_word):
    key_word = key_word.lower()
    if key_word in data:
        return data[key_word]
    else:
        return "The word does not exist"


word = input("Enter the word:")
print(return_one_word(word))
