# No.1 application: Interactive dictionary

import json
from difflib import get_close_matches as gcm

data = json.load(open("files/data.json"))


def return_definition(searched_word, definitions):
    def_number = 1
    print("There are %s definitions for the word %s: " % (len(definitions[searched_word]), searched_word))
    if len(definitions[searched_word]) == 1:
        print("No %s: " % def_number + str(definitions[searched_word][0]))
    else:
        for item in definitions[searched_word]:
            print("No %s: " % def_number + str(item))
            def_number = def_number +1


def translate(key_word):
    key_word = key_word.lower()
    if key_word.lower() in data:
        return_definition(key_word, data)
    elif key_word.title() in data:
        return_definition(key_word.title(), data)
    elif key_word.upper() in data:
        return_definition(key_word.upper(), data)
    elif len(gcm(key_word, data.keys())) > 0:
        user_input = input("Did you mean %s instead? Enter Y if yes or N if no: " % gcm(key_word, data.keys(), cutoff=0.8)[0])
        if user_input.upper() == "Y":
            return_definition(gcm(key_word, data.keys(), cutoff=0.8)[0], data)
        elif user_input.upper() == "N":
            print("The word does not exist please double check it")
        else:
            print("You did not answer with yes or no")
    else:
        print("The word does not exist. Please double check it")


word = input("Enter the word:")
translate(word)
