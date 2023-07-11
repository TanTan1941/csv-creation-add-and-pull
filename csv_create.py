import csv

with open('names.csv' , mode="w") as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()