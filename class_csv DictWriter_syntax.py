# Class csv.DictWriter
# An example of csv.DictWriter
import csv

with open('companies.csv', 'w') as csvfile:
  fieldnames = ['name', 'type']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'name': 'Codecademy', 'type': 'Learning'})
  writer.writerow({'name': 'Google', 'type': 'Search'})

"""
After running the above code, companies.csv will contain the following information:

name,type
Codecademy,Learning
Google,Search


In Python, the csv module implements classes to read and write tabular data in CSV format. It has a class DictWriter
which operates like a regular writer but maps a dictionary onto output rows. The keys of the dictionary are column names
while values are actual data.

The csv.DictWriter constructor takes two arguments. The first is the open file handler that the CSV is being written to.
The second named parameter, fieldnames, is a list of field names that the CSV is going to handle.

"""
