#CCIR Phase 1 Section 3 Task 1

import json

# parsing JSON:
x = '{"Name": "Aarav", "age": "16", "city": "New Delhi"}' # x is a string
print(type(x))
y = json.loads(x) # y is a python object (dict)
print(type(y))
print(y["age"])


# Outputing JSON
a = {
    "name": "Jahaan",
    "age": 11,
    "city": "Ludhiana"
} # a is a Python object (dict)
b = json.dumps(x) # converts into JSON string
print(type(y))