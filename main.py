"""
COMP 348: Assignment 2
Name: Asifur Rahman
Student ID: 40194283
"""

import sys

from operations.display_menu import main_menu
from operations.display_statistics import *
from operations.process_data import read_files


def main(file_name):
    operate(read_files(file_name))


def operate(data):
    run = True
    while run:
        menu_choice = main_menu()

        if menu_choice == 1.0:
            show_global(data)
        elif menu_choice == 2.0:
            print("Enter the submenu keys: 2.1 or 2.2")
        elif menu_choice == 2.1:
            show_random_station_statistics(data)
        elif menu_choice == 2.2:
            station_id = int(input("Please enter the id of the station you wish to see: "))
            show_station_statistics_by_id(data, station_id)
        elif menu_choice == 3.0:
            lat = float(input("Enter the latitude: "))
            lon = float(input("Enter the longitude: "))
            show_coverage(data, lat, lon)
        elif menu_choice == 4.0:
            print("Exiting program.")
            run = False
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error! Please use the following format: ")
        print("python3 assignment2.py <test_file.json>")
        sys.exit(1)
    json_file = sys.argv[1]
    main(json_file)
