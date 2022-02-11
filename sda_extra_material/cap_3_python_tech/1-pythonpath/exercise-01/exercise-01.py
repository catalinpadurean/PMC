r"""
1. Examine given example. Look at its modules, `__init__.py` and `__main__.py` files.
<skipped>
2. Write a simple script (it has to be in `exercise-01` directory) which imports `happy_symbol` from `examplepackage.symbols`. What happens when you run it?
>>> from examplepackage.symbols import happy_symbol
<BLANKLINE>
Entering examplepackage/__init__.py
<BLANKLINE>
This file will be executed on every `import examplepackage`.
This means it will also be executed when running __main__.py.
<BLANKLINE>
>>> print(happy_symbol)
😁

3. Try importing `from examplepackage.symbols import *`. What did it import?
>>> from examplepackage.symbols import *
>>> all(x in globals() for x in ["happy_symbol", "sad_symbol", "confused_symbol", "all_symbols"])
True

4. Try executing examplepackage: `python3 -m examplepackage`. What does it do?
<skipped>

Other tests:
>>> print(all_symbols)
('😁', '😢', '😕')

>>> import examplepackage
>>> all(examplepackage.functions.is_symbol(s) for s in all_symbols)
True
    
"""
