# Execute while body block as long as n < 5
n = 0
while n < 5:
    n += 1  # increment n with each loop execution
    print(n)

# Execute while body block as long as n < 5
n = 0
while n < 5:
    n += 1  # increment n with each loop execution
    if n == 4:  # if n is 4 then exit the loop
        break
    if n == 1:  # if n is 1 then start next iteration
        continue
    print(n)

# Execute while body block as long as n < 5
n = 0
while n < 5:
    n += 1  # increment n with each loop execution
    print(n)
else:
    print("Done.")  # print out Done. only when while loop condition is exhausted
