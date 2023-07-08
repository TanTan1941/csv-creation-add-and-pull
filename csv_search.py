print('running')
import csv

print('still running')
def search_user():
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    with open('names.csv', 'r') as file:
        data = csv.reader(file)
        for row in data:
            if len(row) >= 2:  # Check if row has at least two columns
                if first_name == row[0] and last_name == row[1]:
                    print('Welcome!')
                    return True
    return False

print('done')

start = int(input('Press 1 for login '))

if start == 1:
    if search_user():
        print('Welcome Nerd')
    else:
        print('Access Denied')
else:
        print('Invalid User Input')
