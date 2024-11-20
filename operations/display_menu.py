"""
COMP 348: Assignment 2
Name: Asifur Rahman
Student ID: 40194283
"""


def main_menu():
    print("""
    1. Display Global Statistics
    2. Display Base Station Statistics
        2.1. Statistics for a random station
        2.2. Choose a station by Id.
    3. Check Coverage
    4. Exit
    """)
    return float(input("Enter your choice: "))
