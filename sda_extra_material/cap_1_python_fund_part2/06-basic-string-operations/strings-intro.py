# Print out amount of characters in the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(len(sentence))  # prints out 29

# Print out index of first 'o' character in the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence.index("o"))  # prints out 1

# Print out amount of 'o' characters in the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence.count("o"))  # prints out 3

# Print out 4th character of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[3])  # prints out e

# Print out 'm ips' substring of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[4:9])  # prints out 'm ips'

# Print out 'um dolor sit amet...' substring of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[9:])  # prints out 'um dolor sit amet...'

# Print out 'Lorem ip' substring of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[:8])  # prints out 'Lorem ip'

# Print out 'mis' substring of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[4:9:2])  # prints out 'mis'

# Print out the sentence in reverse order
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[::-1])  # prints out '...tema tis rolod muspi meroL'

# Print out the sentence in uppercase
sentence = "Lorem ipsum dolor sit amet..."
print(sentence.upper())  # prints out the sentence in uppercase

# Print out the sentence in lowercase
sentence = "Lorem ipsum dolor sit amet..."
print(sentence.lower())  # prints out the sentence in lowercase
