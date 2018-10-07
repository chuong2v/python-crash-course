filename = 'alice.txt'
try:
  with open(filename) as f_obj:
    contents = f_obj.read()
except Exception as exp:
  msg = "Sorry, the file " + filename + " does not exist."
  print(msg)
  print(type(exp).__name__)