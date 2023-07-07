import csv

with open('names.csv' , mode="a") as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"first_name": "janey", "last_name": "doe"})
    writer.writerow({"first_name": 'johnathon', "last_name": "Beans"})