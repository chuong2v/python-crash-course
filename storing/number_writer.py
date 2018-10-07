import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
numbers = [2, 3, 5, 7, 11, 13]
filename = dir_path + '/numbers.json'
with open(filename, 'w') as file_object:
  json.dump(numbers, file_object)