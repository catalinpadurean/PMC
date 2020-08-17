# No.1 application: Interactive dictionary

import json
import difflib # library to compare text
from difflib import SequenceMatcher as sqm  # import only SequenceMatcher from library
from difflib import get_close_matches as gcm  # import only get_close_matches from library


data = json.load(open("files/data.json"))
# print(help(SQM))
# print((help(GCM)))

# print(gcm("rainn", ["rainn", "pyramid", "rrain", "raaain"], 2, 0.7))
# print(gcm("rain", data.keys(),5,0.2))

# print(sqm(None, "rain", "rainn").ratio())
# SQM.ratio() will return the similarity between the strings passed as parameters. The value is between 0 and 1

# Add similarity ration between words to the existing code


def return_one_word(key_word):
    key_word = key_word.lower()
    if key_word in data:
        return data[key_word]
    elif len(gcm(key_word, data.keys())) > 0:
        return "Did you mean %s instead?" % gcm(key_word, data.keys(), cutoff=0.8)[0]
    else:
        return "The word does not exist. Please double check it"


word = input("Enter the word:")
print(return_one_word(word))
