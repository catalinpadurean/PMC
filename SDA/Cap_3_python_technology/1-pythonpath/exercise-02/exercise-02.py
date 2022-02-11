import sys

assert "../exercise-01" not in sys.path
try:
    import examplepackage
except ModuleNotFoundError:
    print("Module not found, as expected.")
else:
    print("That should not happen!")

print("Extending sys.path...", end=" ")
sys.path.append("../exercise-01")
print("OK")

print("Importing examplepackage")
import examplepackage

print(
    f"{examplepackage.symbols.happy_symbol}\tis a symbol: ",
    f"{examplepackage.functions.is_symbol(examplepackage.symbols.happy_symbol)}",
)
