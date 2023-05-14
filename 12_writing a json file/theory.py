"""

Learn Python: Files
Writing a JSON File

Naturally we can use the json library to translate Python objects to JSON as well. This is especially useful in
instances where you’re using a Python library to serve web pages, you would also be able to serve JSON. Let’s say we had
a Python dictionary we wanted to save as a JSON file:
"""
turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}
"""
We’d be able to create a JSON file with that information by doing the following:
"""
import json

with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)
"""
We import the json module, open up a write-mode file under the variable json_file, and then use the json.dump() method
to write to the file. json.dump() takes two arguments: first the data object, then the file object you want to save.
Instructions
1.

In your workspace, we’ve put a dictionary called data_payload. We want to save this to a file called data.json.

Let’s start by importing the json library.
2.

Open a new file object in the variable data_json. The filename should be 'data.json' and the file should be opened in
write-mode.

Remember to open a file in write-mode with the following syntax:
"""
with open('file.json', 'w') as file_json:
  pass
"""
3.

Call json.dump() with data_payload and data_json to convert our data to JSON and then save it to the file data.json.

Using json.dump() with the file object as a second argument writes the resulting JSON to the file:
"""
payload = {'message': 'OK'}
with open('file.json', 'w') as file_json:
  json.dump(payload, file_json)
"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
