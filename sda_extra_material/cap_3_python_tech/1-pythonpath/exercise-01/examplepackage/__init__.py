"""
Entering examplepackage/__init__.py

This file will be executed on every `import examplepackage`.
This means it will also be executed when running __main__.py.
"""
from .functions import list_symbols, is_symbol
from .symbols import *
# print("Init file has been used")
# print(__doc__)
print("Init se executa de fiecare data cand pachetul este folosit in orice mod")

