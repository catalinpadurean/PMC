#Linkuri utile:
# 0. https://realpython.com/python-while-loop/
# 1. https://www.w3schools.com/python/python_for_loops.asp
animals = ["Dog", "Cat", "Fish" ]
plants = ["tomato", "pepper", "onion", "brocoli"]
objects = ["pen", "pencil", "keyboard", "glass"]

print("Lista animale: ")
# Print out all animals in the list
for variabila_test in animals:
    print(variabila_test.upper())  # prints out a single animal
print("Lista legume: ")
for variabila_test in plants:
    print(variabila_test.upper())  # prints out a single vegetable

print("Lista obiecte: ")
for variabila_test in objects:
    print(variabila_test.upper())  # prints out a single object

# contor_lista = 0
# iterator_lista = ""
# while contor_lista < len(animals):
#     iterator_lista = animals[contor_lista]  # contor =0, iterator = dog
#     if contor_lista == 1:
#         print("Am ajuns la elementul 1")
#     if iterator_lista == "Fish":
#         print("Am ajuns la elementul fish")
#
#     print("contorul listei: ", contor_lista)
#     print(f"pentru contorul {contor_lista} elementul este {iterator_lista}")
#     contor_lista = contor_lista + 1
# else:
#     print("Am terminat de parcurs lista cu animale")


# sum = 0
# prod = 1
# for i in range(0, 6, 1):
#     userInput = int(input(f"Introduceti numarul {i}:" ))
#     sum = sum + userInput
#     prod = prod * userInput
# print("SUM: ", sum)
# print("PROD: ", prod)

# animals = ["Dog", "Cat", "Fish" ]
#           # 0       1       2
#
# for i in range(len(animals)):
#     print(i*20)

# # Print -3, -2, -1, 0
# for i in range(-3, 1):
#     print(i)

# # Print 3, 5, 7, 9
# for i in range(0, 11, 2):
#     print(i)
#
# # # Print -1, -2, -3
# for i in range(-1, -4, -1):
#     print(i)
#
# test_var = range(0, 12)
# print(type(test_var))
# print(help(range))
