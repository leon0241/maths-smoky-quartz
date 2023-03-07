import os
import re

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
      edit_fields(appended)

def edit_fields(filename):
  with open(filename, 'r+') as f:
    text = f.readlines()

    for i, line in enumerate(text):
      backlink_search = re.search("(?!\[[^\]]*\])\(.+?(?:md)\)", line)
      if (backlink_search != None):
        post_string = backlink_search.group().replace("\\", "/")
        text[i] = re.sub("(?!\[[^\]]*\])\(.+?(?:md)\)", post_string, line)

    f.seek(0)
    f.writelines(text)
    f.truncate()


recursive_search("content")

# edit_fields("Content/Individuals/Quadrature Rules.md")
