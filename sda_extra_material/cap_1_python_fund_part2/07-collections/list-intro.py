# Declare and initialize a list variable
alphabet = []  # this is an empty list
print(f"Current length of 'alphabet': {len(alphabet)}")

# Add some letters
alphabet.append("a")
alphabet.append("b")
alphabet.append("c")
print(f"Alphabet: {alphabet} (length: {len(alphabet)})")

# Indexing
print(f"The first letter of alphabet is '{alphabet[0]}'")

# Add some more letters
alphabet.extend(["f", "d", "g", "e"])
print(f"Alphabet (mixed): {alphabet} (length: {len(alphabet)})")

# Sort the list
alphabet.sort()
print(f"Alphabet (sorted): {alphabet} (length: {len(alphabet)})")
