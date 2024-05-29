#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """Writes string to text file and returns number of characters"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
