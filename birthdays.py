"""
This module provides a simple birthday dictionary and functions
to display available names and retrieve a person's birthday.
"""
import calendar
import csv

def get_birthdays():
    birthdays = {}

    with open('birthdays.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            birthdays[row['names']] = row['birthdays']

    return birthdays


def print_birthdays():
    """Prints a welcome message and lists all the names in the birthday dictionary."""
    birthdays = get_birthdays()
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    """Prints the birthday of the given person if present in the dictionary,
        otherwise informs the user that the birthday is not available."""
    birthdays = get_birthdays()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

def add_birthday_entry(name, birthday):
    """Adds a new person and birthday to the birthdays dictionary."""
    birthdays = get_birthdays()
    birthdays[name] = birthday

def leap_year_birthdays():
    """Returns a list of names born in leap years."""
    leap_people = []
    birthdays = get_birthdays()
    for name, date in birthdays.items():
        month, day, year = date.split('/')
        year = int(year)

        if calendar.isleap(year):
            leap_people.append(name)

    return leap_people