import json
import os
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
dir_path = os.path.dirname(os.path.realpath(__file__))

def get_stored_username():
  """Get stored username if available."""
  filename = dir_path + '/username.json'
  try:
    with open(filename) as f_obj:
      username = json.load(f_obj)
  except FileNotFoundError:
    return None
  else:
    return username

def greet_user():
  """Greet the user by name"""
  username = get_stored_username()
  if username:
    print("Welcome back, " + username + "!")
  else:
    username = input("What is your name? ")
    filename = dir_path + '/username.json'
    with open(filename, 'w') as f_obj:
      json.dump(username, f_obj)
      print("We'll remember you when you come back, " + username + "!")

greet_user()