#!/usr/bin/python3
"""
Contains method inherits_from
returns True if obj is instance of class that it inherits from or is subcls of
"""

def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class ; otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
