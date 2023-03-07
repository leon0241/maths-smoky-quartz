import os

def recursive_search(root):
  # For  each item in the root
  for filename in os.listdir(root):
    # Traverse 1 layer
    appended = root + "/" + filename
    
    # If filename is a folder, recursively call
    if (os.path.isdir(appended)):
      recursive_search(appended)
    
    # If it's a markdown file then run function. Else nothing.
    elif (filename.endswith('.md')):
      append_eof(appended)

def append_eof(filename):
  with open(filename, 'r+') as f:
    text = f.readlines()
    if (text[-1] == "%%EOF%%"):
      f.write("\n%%EOF%%")

recursive_search("vault")