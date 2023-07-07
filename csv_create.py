import csv

with open('names.csv' , mode="w") as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"first_name": "john", "last_name": "doe"})
    writer.writerow({"first_name": 'jane', "last_name": "doe"})