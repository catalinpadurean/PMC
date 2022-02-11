# The if statement
x = 0
y = 3

if x > y:  # evaluates to false, message is not displayed
    print(f"{x} is greater than {y}")

if x < y:  # evaluates to true, message is displayed
    print(f"{x} is lesser than {y}")

# The if-else statements
x = 0
y = 3

if x > y:  # evaluates to false, message is not displayed
    print(f"{x} is greater than {y}")

else:  # is executed when if statement evaluates to false, message is displayed
    print(f"{x} is less than {y}")

# The if-elif-else statements
x = 0
y = 3

if x > y:  # evaluates to false, message is not displayed
    print(f"{x} is greater than {y}")
elif x == 3:  # evaluates to false, message is not displayed
    print(f"{x} is equal to {y}")
else:  # is executed when none of the if/elif statement evaluates to true, message is displayed
    print(f"{x} is less than {y}")
