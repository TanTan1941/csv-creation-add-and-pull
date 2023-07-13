import csv


def add():
    user = input('First name:')
    passwd = input('Last name: ')
    csvfile = open('names.csv', mode='a')
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerow({'first_name': user, 'last_name': passwd})

    csvfile.close()
    
    done = print('User Added')

    factor

factor = int(input("Press '1' to start adding users: "))


while factor == 1:
    add()
    factor = int(input("Press '1' to continue adding users: "))
if factor != 1:
    exit
    print('Exiting process')

