# input_string = "Python is a really nice language."
input_string = "Python is a really nice language"

# Calculate remainder of division by 2 to know if input_string length is odd or even
# if the remainder is 0, length is even, otherwise odd
remainder = len(input_string) % 2

# Define amount of letters that should be displayed in each direction (right, left) from the middle of the input_string
amount_of_letters = 2

# Calculate middle index of the input_string by dividing the length by 2 and rounding down (e.g. 7.5 -> 7)
middle_index = int(len(input_string) / 2)

# Calculate start index of the substring by subtracting amount of letters from middle index
start_index = middle_index - amount_of_letters

# Calculate end index of the substring by adding amount of letters to middle index and adding the remainder
# if the remainder is 0 (input_string is even) then we have a substring of 4 chars, otherwise we have a substring of 5 chars
end_index = middle_index + amount_of_letters + remainder

# Calculate result by retrieving substring from input_string
result = input_string[start_index:end_index]
#
# # Print out the result
# print(f"Result: '{result}'")

print(help(int))
