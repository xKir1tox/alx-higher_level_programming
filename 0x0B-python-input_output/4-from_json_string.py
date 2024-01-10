#!/usr/bin/python3
"""function that returns an object (Python data structure) represented by a JSON string  """
import json
def from_json_string(my_str):
    """ Function that returns the JSON representation of an object
    Args:
        my_str: object
    Raises:
        Exception: when the object can't be encoded
    """
    return json.loads(my_str)