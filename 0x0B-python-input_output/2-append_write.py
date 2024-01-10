#!/usr/bin/python3
""" Module that contains a function that append on a file """
def append_write(filename="", text=""):
    """ Function that reads from a file
    Args:
         filename: filename
        text: text to append
    Raises
        Exception: when the file can be opened
    """
    with open(filename,'a',encoding='utf-8') as f:
        return f.write(text)