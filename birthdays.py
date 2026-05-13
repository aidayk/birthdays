"""
This module provides a simple birthday dictionary and functions
to display available names and retrieve a person's birthday.
"""
import calendar

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    """Prints a welcome message and lists all the names in the birthday dictionary."""
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    """Prints the birthday of the given person if present in the dictionary,
        otherwise informs the user that the birthday is not available."""
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

def add_birthday_entry(name, birthday):
    """Adds a new person and birthday to the birthdays dictionary."""
    birthdays[name] = birthday

def leap_year_birthdays():
    """Returns a list of names born in leap years."""
    leap_people = []

    for name, date in birthdays.items():
        month, day, year = date.split('/')
        year = int(year)

        if calendar.isleap(year):
            leap_people.append(name)

    return leap_people