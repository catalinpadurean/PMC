# Linkuri utile
# 0. https://realpython.com/python-strings/
# 1. https://www.w3schools.com/python/python_ref_string.asp
# 2. https://www.programiz.com/python-programming/methods/built-in/id

print("!"*100)
print("Note: All string methods returns new values. They do not change the original string.")
print("!"*100)

# Print out amount of characters in the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(len(sentence))  # prints out 29

# Print out index of first 'o' character in the sentence
sentence = "Lorem ipsum dolor sit amet..."
# print(sentence.iondex(""))  # prints out 1

# Print out amount of 'o' characters in the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence.count("o"))  # prints out 3

# Print out 4th character of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[28])  # prints out e
ultim_index = len(sentence)-1

# Print out 'm ips' substring of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[4:9])  # prints out 'm ips'
# print(sentence[10:10])  # prints out 'm ips'

# Print out 'um dolor sit amet...' substring of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[9:])  # prints out 'um dolor sit amet...'

# Print out 'Lorem ip' substring of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[:8])  # prints out 'Lorem ip'

# Print out 'mis' substring of the sentence
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[::3])  # prints out 'mis'

# Print out the sentence in reverse order
sentence = "Lorem ipsum dolor sit amet..."
print(sentence[::-1])  # prints out '...tema tis rolod muspi meroL'
sent_2 = "abcdefghi"
#Pos_idx  012345678
#Neg_idx  987654321

print(sent_2[1:4][::-1])

# Print out the sentence in uppercase
sentence = "Lorem ipsum dolor sit amet...Α α, β, Γ γ, Δ δ, "
print(sentence.upper())  # prints out the sentence in uppercase

# Print out the sentence in lowercase
sentence = "Lorem ipsum dolor sit amet..."
print(sentence.lower())  # prints out the sentence in lowercase


"""Extra examples"""
# String slicing

# If the first index in a slice is greater than or equal to the second index, Python returns an empty string.
word_1 = "python"
print(word_1[3:3])
print(word_1[-5:-7])

# # Slicing using negative indexing. Negative indexes count from len(w) to 1. Positive indexes count from 0 to len(w)-1

word_3 = "absolute"
# Pos_idx 01234567
# Neg_idx 87654321
print(word_3[1:4])
print(word_3[-7:-4])

# # Slicing strings with stride

word_4 = "THiS WaS JuSt aNother simple sentence"
print(word_4[::2])
# You can specify a negative stride value as well, in which case Python steps backward through the string.
# In that case, the starting/first index should be greater than the ending/second index:
print(word_4[15])
print(word_4[1])
print(word_4[15:1:-2])
print(word_4[1:12:2])
