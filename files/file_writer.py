import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/programming.txt', 'w') as file_object:
  file_object.writelines('I love programming.\n')
  file_object.write('I love Python.\n')