!#/usr/bin/env/ python
import os
import re

def crear_directorio(directorio):
  assert type(directorio) == str, 'Directory name must be a string'
  #return the corresponding pwd, if exists, then we only change our directory if not, we create a new one///
  if os.path.exists(directorio) == False:
    os.mkdir(directorio)
    os.chdir(directorio)
    return os.getcwd()
  else:
    os.chdir(directorio)
    print('This directory already exists')
    return os.getcwd()
def check_file(file):
  assert type(file) == str, 'Directory name must be a string'
  result = re.search(r"(.*[\.]py) , file)
  if result == None
    raise TypeError('File must be a python file')
  return result[0]
def join(directorio, file)
  if os.path.exists(file) == False:
    os.path.join(directorio,file)
    with open(file, 'w') as file1:
      file1.write('#/usr/bin/env/ python')
  else:
    print('File already exists')
if __name__ == '__main__':
  directory = str(input('Directory: '))
  file =  str(input('File: ')
  crear_directorio(directory)
  check_file(file)
  join(directory, file)
  
