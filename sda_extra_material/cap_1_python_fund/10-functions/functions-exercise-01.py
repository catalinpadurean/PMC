def max_of_three(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

var1_test = (max_of_three(1,5,6))
var2_test = (max_of_three(4,2,4))
print(max_of_three(100,200,300))

