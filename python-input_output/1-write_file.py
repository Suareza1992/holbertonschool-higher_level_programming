#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file and returns the number of characters"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
