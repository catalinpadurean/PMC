user_input = ""

# b. If the input is equal to “exit”, program terminates printing out provided input and “Done.”.
while user_input != "exit":
    # a. Asks user for an input in a loop and prints it out.
    user_input = input("Provide input: ")
    # c. If the input is equal to “exit-no-print”, program terminates without printing out anything.
    if user_input == "exit-no-print":
        break
    # d. If the input is equal to “no-print”, program moves to next loop iteration without printing anything.
    if user_input == "no-print":
        continue
    # a. Asks user for an input in a loop and prints it out.
    # b. If the input is equal to “exit”, program terminates printing out provided input and “Done.”.
    # e. If the input is different than “exit”, “exit-no-print” and “no-print”, program repeats.
    print(user_input)
else:
    # b. If the input is equal to “exit”, program terminates printing out provided input and “Done.”.
    print("Done.")


#Exercitii suplimentare:

# Cereti utilizatorului sa introduca de la tastatura exact 12 numere si sa calculeze suma si produsul acestora
