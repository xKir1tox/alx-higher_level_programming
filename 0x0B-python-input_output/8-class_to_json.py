#!/usr/bin/python3
""" My class module
"""
def class_to_json(obj):
    """ Function that creates an Object from a JSON file
    Args:
        obj: object
    Raises:
        Exception: when the object can't be encoded
    """
    return obj.__dict__
