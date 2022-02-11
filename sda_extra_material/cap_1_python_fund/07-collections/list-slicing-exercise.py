users = ["User1", "UserChris", "User2", "Admin"]

# a. Print out a slice containing only “User2”.
print(users[2:3])

# b. Print out a slice of all users, except the first one.
print(users[1:])

# c. Print out a slice of all users, except the “Admin”.
print(users[:len(users) - 1])

# d. Print out a slice of all users up to the 3rd one.
print(users[:2])
