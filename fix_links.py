import os

# Recursively search each folder for markdown files
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
      edit_fields(filename)

def edit_fields(filename):
  with open(filename, 'r') as f:
    text = f.readlines()
    print(text)

# recursive_search("content")

edit_fields("Content/Mathematics/Groups.md")