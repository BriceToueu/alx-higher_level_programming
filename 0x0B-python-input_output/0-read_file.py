#!/usr/bin/python3
# File: 0-read_file.py
# Auth: Brice Toueu

"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
