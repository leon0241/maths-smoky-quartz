import os
import re

REGEX_LINK_SEARCH = "(?!\[[^\]]*\])\(.+?(?:md)"
REGEX_TAG_SEARCH = "\*{2}Tags:\*{2}"
REGEX_LINKER_SEARCH = "\^.{6}\\n"
REGEX_EOF_SEARCH = "%%EOF%%"

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

    initial_tag_passed = False
    delete_within = False
    frontmatter_tag_storage = ""

    for i, line in enumerate(text):

      tag_search = re.search(REGEX_TAG_SEARCH, line)

      # If regex finds a tag, and it's the first set of tags
      if (tag_search != None and initial_tag_passed == False):
        initial_tag_passed = True
        frontmatter_tag_storage = tag_search.group()
      # If regex finds a tag then it's left over from delete it :p
      elif (tag_search != None):
        text[i] = ""
        continue

      eof_search = re.search(REGEX_EOF_SEARCH, line)
      if (eof_search != None):
        text[i] = ""
        delete_within = False
        continue

      if (delete_within == True):
        text[i] = ""
        continue


      link_search = re.search(REGEX_LINKER_SEARCH, line)
      if (link_search != None):
        delete_within = True
        text[i] = ""
        continue

      backlink_search = re.search(REGEX_LINK_SEARCH, line)
      if (backlink_search != None):
        post_string = backlink_search.group().replace("\\", "/")
        text[i] = re.sub(REGEX_LINK_SEARCH, post_string, line)

    text = list(filter(None, text))
    # print(text)
    f.seek(0)
    f.writelines(text)
    f.truncate()

edit_fields("Content/Individuals/Applications of Lagrange.md")

recursive_search("content")