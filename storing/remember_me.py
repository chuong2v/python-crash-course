import json
import os
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + '/username.json'

try:
  with open(filename) as f_obj:
    username = json.load(f_obj)
except FileNotFoundError:
  username = input("What is your name? ")
  with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else:
  print("Welcome back, " + username + "!")