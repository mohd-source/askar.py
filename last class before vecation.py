import csv
import pandas as pd

fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [
    {'Name': 'Nikhil',  'Branch': 'COE', 'Year': '2', 'CGPA': '9.0'},
    {'Name': 'Sanchit', 'Branch': 'COE', 'Year': '2', 'CGPA': '9.1'},
    {'Name': 'Aditya',  'Branch': 'IT',  'Year': '2', 'CGPA': '9.3'},
    {'Name': 'Sagar',   'Branch': 'SE',  'Year': '1', 'CGPA': '9.5'},
    {'Name': 'Prateek', 'Branch': 'MCE', 'Year': '3', 'CGPA': '7.8'},
    {'Name': 'Sahil',   'Branch': 'EP',  'Year': '2', 'CGPA': '9.1'}
]

filename = "Uni__Record.csv"

with open(filename, 'r', ) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        print(row)

