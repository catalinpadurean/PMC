# Putting the pieces together: building a program
# create a function that receives a string and turns it into sentence (capitalizez first word and adds . at the end or question mark)


def sentence_maker(phrase):
    interrogatives = ("how","what","why", "who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


# print(sentence_maker("how are you"))


def first_program():
    user_input_list=[]
    while True:
        user_input = input("Say something: ")
        if user_input == "\end":
            break;
        else:
            user_input_list.append(sentence_maker(user_input))
            continue
    for item in user_input_list:
        print(item)


first_program()



