import os
import sys

print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")
print("Trying to import examplepackage")

sys.path.append(r"J:\Work\SDA\Cap_3_python_technology\1-pythonpath\exercise-01")
# sys.path.append("../exercise-01")
import examplepackage
print("Success!")
