#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation  """
import json
def save_to_json_file(my_obj, filename):
    """ Function that returns the JSON representation of an object
    Args:
        my_obj: object
        filename : object
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)