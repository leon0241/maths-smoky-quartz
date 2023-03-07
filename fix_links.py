import os
import re

REGEX_LINK_SEARCH = "(?!\[[^\]]*\])\(.+?(?:md)"
REGEX_TAG_SEARCH = "\*{2}Tags:\*{2}"
REGEX_LINKER_SEARCH = "'\^.{6}\\n'"

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

    delete_within = False

    for i, line in enumerate(text):

      tag_search = re.search(REGEX_TAG_SEARCH, line)
      if (tag_search != None and delete_within == True):
        delete_within = False
        text[i] = ""
        break

      if (delete_within == True):
        text[i] = ""
        break


      link_search = re.search(REGEX_LINKER_SEARCH, line)
      if (link_search != None):
        delete_within = True
        text[i] = ""
        break

      backlink_search = re.search(REGEX_LINK_SEARCH, line)
      if (backlink_search != None):
        post_string = backlink_search.group().replace("\\", "/")
        text[i] = re.sub(REGEX_LINK_SEARCH, post_string, line)

    print(text)
    # f.seek(0)
    # f.writelines(text)
    # f.truncate()

edit_fields("Content/Mathematics/Proving a Series is convergent.md")

# recursive_search("content")