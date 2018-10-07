import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + '/numbers.json'

with open(filename, 'r') as file_object:
  numbers = json.load(file_object)

print(numbers)