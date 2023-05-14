# Parsing JSON files to dictionary

# Use json.load with an opened file object to read the contents into a Python dictionary.

# Contents of file.json
# { 'userId': 10 }


import json
with open('file.json') as json_file:
  python_dict = json.load(json_file)

print(python_dict.get('userId'))
# Prints 10

"""
JSON format is used to store key value pairs. Python’s json module allows reading such data format and parsing it to
a dictionary. The json.load function takes a file object as an argument and returns the data in a dictionary format.
"""
