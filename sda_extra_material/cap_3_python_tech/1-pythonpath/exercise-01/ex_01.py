"""Write a simple script (it has to be in exercise-01 directory) which imports happy_symbol from
examplepackage.symbols. What happens when you run it?"""

from examplepackage.symbols import happy_symbol
print(happy_symbol)

try:
    print(5/0)
except ZeroDivisionError:
    print("Nu putem imparti la 0")
