import sys
import examplepackage
print(sys.path)
sys.path.append("../exercise-01")
print(sys.path)
import examplepackage
print(
    f"{examplepackage.symbols.happy_symbol}\tis a symbol: ",
    f"{examplepackage.functions.is_symbol(examplepackage.symbols.happy_symbol)}",
)
# print(sys.path)

