import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + '/pi_digits.txt'
with open(filename) as file_object:
  contents = file_object.read()
  print(contents)

with open(filename) as file_object:
  for line in file_object:
    print(line) # line.rstrip()

with open(filename) as file_object:
  lines = file_object.readlines()

for line in lines:
  print(line)

# Million digits

milion_digits_filename = dir_path + '/pi_million_digits.txt'
with open(milion_digits_filename) as file_object:
  lines = file_object.readlines()
pi_string = ''
for line in lines:
  pi_string += line.rstrip()
print(pi_string[:52] + '...')
print(len(pi_string))


# Is your birthday contained in Pi
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
  print("Your birthday appears in the first million digits of pi!")
else:
  print("Your birthday does not appear in the first million digits of pi.")

