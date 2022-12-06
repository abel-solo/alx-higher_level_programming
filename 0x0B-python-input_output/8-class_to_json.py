#!/usr/bin/python3
"""
returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """uses the built-in vars() method to return
    the __dict__ attribute of obj
    Args:
        obj (Class): object to return changeable attributes
    """
    return vars(obj)
