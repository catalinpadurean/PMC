#Linkuri utile:
# 0. https://www.w3schools.com/python/python_conditions.asp
# 1. https://realpython.com/python-conditional-statements/

# The if statement
x = 0
y = 3

# if x < y:  # evaluates to false, message is not displayed
#     print(f"{x} is greater than {y}")
# if x == y:
#     print(f"{x} is lesser than {y}. Message 1")
# if x > y:  # evaluates to true, message is displayed
#     print(f"{x} is lesser than {y}")
#     print(f"{x} is lesser than {y}. Message 2")

# # The if-else statements
# x = 0
# y = 3
#
# if x > y:  # evaluates to false, message is not displayed
#     print(f"{x} is greater than {y}")
#
# else:  # is executed when if statement evaluates to false, message is displayed
#     print(f"{x} is less than {y}")
# #
# # The if-elif-else statements
# x = 0
# y = 3
#
# if x > y:  # evaluates to false, message is not displayed
#     print(f"{x} is greater than {y}")
# elif x == 3:  # evaluates to false, message is not displayed
#     print(f"{x} is equal to {y}.1")
# elif y % 2 == 1:  # evaluates to false, message is not displayed
#     print(f"{y} e impar")
# else:  # is executed when none of the if/elif statement evaluates to true, message is displayed
#     print(f"{x} is less than {y}.3")

# if (x < y) or (x != 5) :
#     print("Nivel 1")
#     x = 7
#     if x != 5:
#         print("Nivel 2")
#     else:
#         print("Nivel 2 false")