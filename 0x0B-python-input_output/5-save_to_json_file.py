#!/usr/bin/python3
# File: 5-save_to_json_file.py
# Auth: Brice Toueu

"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
