import csv


birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'
}


def write_birthdays():
    with open('birthdays.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['names', 'birthdays'])

        for name, birthday in birthdays.items():
            writer.writerow([name, birthday])


write_birthdays()