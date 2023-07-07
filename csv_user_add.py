import csv

user = input('First name:')
passwd = input('Last name: ')

csvfile = open('names.csv', mode='w')
fieldnames = ['first_name', 'last_name']
writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
writer.writerow({'first_name': user, 'last_name': passwd})