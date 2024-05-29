#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """Appends string at end of text and returns number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
