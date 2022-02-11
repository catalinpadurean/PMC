words_dict = {}

with open("data/exercise.txt") as f:  # f is a file object
    for i, line in enumerate(f):  # iterate every line of the file
        if i == 0:  # skip first line
            continue

        clean_line = line.rstrip()  # remove "\n" - end of line character at the end of each line
        clean_line = clean_line.lower()  # bring all characters to lowercase

        if clean_line == "":  # skip empty lines
            continue

        for char in (".", ",", "!", "?"):  # remove unwanted characters
            clean_line = clean_line.replace(char, "")

        words = clean_line.split(" ")  # split string into a list of words

        for word in words:  # for each word in the list, add it to dictionary
            if words_dict.get(word) is not None:  # if the word was in the dictionary before, increment count
                words_dict[word] += 1
            else:  # if the word was not in the dictionary yet, add it and set count to 1
                words_dict[word] = 1

with open("data/result.txt", "w+") as f:  # open file in write mode
    for word in words_dict:
        f.write(f"Word {word} occurred {words_dict[word]} time(s).\n")
