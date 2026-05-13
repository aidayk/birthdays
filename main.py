#! /usr/bin/env python3

#from birthdays import return_birthday
from birthdays import add_birthday_entry
from birthdays import leap_year_birthdays



add_birthday_entry('Erling Haaland', '07/21/2000')
add_birthday_entry('Albert Gore', '03/31/1948')
add_birthday_entry('Elizabeth Bowes-Lyon', '08/04/1900')

print(leap_year_birthdays())