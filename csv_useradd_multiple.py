import csv

factor = input("Press '1' to start adding users: ")

def add():
    user = input('First name:')
    passwd = input('Last name: ')
    csvfile = open('names.csv', mode='a')
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerow({'first_name': user, 'last_name': passwd})
    done = print('User Added')

    csvfile.close()



if factor == '1':
    add()

for done in factor:
    add()
