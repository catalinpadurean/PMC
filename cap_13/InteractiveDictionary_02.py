# No.1 application: Interactive dictionary

import json
from difflib import get_close_matches as gcm

data = json.load(open("files/data.json"))
# print (gcm("CEO",data.keys()))

def dictionary_add_new_entry(new_key, definition):
    dict_data = {}
    dict_data[new_key] = definition
    with open("files/new_words.json", "a+") as new_file:
        json.dump(dict_data,new_file)
    print("Your definition has been submitted for review. Thank you")


def dictionary_ask_new_entry(user_word):
    new_word = input("The word does not exist. Do you want to add the word %s to the dictionary ? Enter Y if yes or N if no: " % user_word)
    if new_word.upper() == "Y":
        new_word_key = user_word
        new_word_def = input("Enter the definition for %s: " % new_word_key)
        dictionary_add_new_entry(new_word_key ,new_word_def)
    elif new_word.upper() == "N":
        print("The word does not exist please double check it")
    else:
        print("You did not enter a valid options")


def dictionary_return_definition(searched_word, definitions):
    def_number = 1
    print("There are %s definitions for the word %s: " % (len(definitions[searched_word]), searched_word))
    if len(definitions[searched_word]) == 1:
        print("No %s: " % def_number + str(definitions[searched_word][0]))
    else:
        for item in definitions[searched_word]:
            print("No %s: " % def_number + str(item))
            def_number = def_number +1


def dictionary_translate(key_word):
    key_word = key_word.lower()
    if key_word in data:
        dictionary_return_definition(key_word, data)
    elif key_word.title() in data:
        dictionary_return_definition(key_word.title(), data)
    elif key_word.upper() in data:
        dictionary_return_definition(key_word.upper(), data)
    elif len(gcm(key_word, data.keys(), cutoff=0.8)) > 0:
        user_input = input("Did you mean %s instead? Enter Y if yes or N if no: " % gcm(key_word, data.keys(), cutoff=0.8)[0])
        if user_input.upper() == "Y":
            dictionary_return_definition(gcm(key_word, data.keys(), cutoff=0.8)[0], data)
        elif user_input.upper() == "N":
            dictionary_ask_new_entry(key_word)
        else:
            print("You did not answer with yes or no")
    else:
        dictionary_ask_new_entry(key_word)


word = input("Enter the word:")
dictionary_translate(word)
