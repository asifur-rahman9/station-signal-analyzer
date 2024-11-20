"""
COMP 348: Assignment 2
Name: Asifur Rahman
Student ID: 40194283
"""

import json


def read_files(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data
