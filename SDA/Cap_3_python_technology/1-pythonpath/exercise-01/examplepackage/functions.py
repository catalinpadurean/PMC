from .symbols import *


def list_symbols():
    """Returns a list of all symbols available."""
    return list(all_symbols)


def is_symbol(symbol):
    """Checks whether a symbol exists."""
    return symbol in all_symbols
