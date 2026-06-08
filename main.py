#! /usr/bin/env python3

import argparse

from birthdays import birthdays
from birthdays import return_birthday

#from birthdays import leap_year_birthdays
#add_birthday_entry('Erling Haaland', '07/21/2000')
#add_birthday_entry('Albert Gore', '03/31/1948')
#add_birthday_entry('Elizabeth Bowes-Lyon', '08/04/1900')
#print(leap_year_birthdays())

firstnames = []
lastnames = []

for name in birthdays:
    firstname, lastname = name.split(maxsplit=1)
    firstnames.append(firstname)
    lastnames.append(lastname)

parser = argparse.ArgumentParser(
    description="Return the birthday of a person stored in the birthday dictionary."
)

parser.add_argument(
    "--firstname",
    required=True,
    choices=firstnames,
    help="Firstname of the person whose birthday is requested."
)

parser.add_argument(
    "--lastname",
    required=True,
    choices=lastnames,
    help="Lastname of the person whose birthday is requested."
)

args = parser.parse_args()

full_name = args.firstname + " " + args.lastname

return_birthday(full_name)