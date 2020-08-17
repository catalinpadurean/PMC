# No.1 application: Interactive dictionary

import json
from difflib import get_close_matches as gcm  # import only get_close_matches from library
data = json.load(open("files/data.json"))

# Add confirmation from the user to the existing code


def return_one_word(key_word):
    key_word = key_word.lower()
    if key_word in data:
        return data[key_word]
    elif len(gcm(key_word, data.keys())) > 0:
        user_input = input("Did you mean %s instead? Enter Y if yes or N if no: " % gcm(key_word, data.keys())[0])
        if user_input == "Y":
            return data[gcm(key_word, data.keys())[0]]
        elif user_input == "N":
            return "The word does not exist please double check it"
        else:
            return "You did not answer with yes or no"
    else:
        return "The word does not exist. Please double check it"


word = input("Enter the word:")
print(return_one_word(word))