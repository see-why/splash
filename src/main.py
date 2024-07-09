import shutil
import os
from generate_page import (generate_pages_recursive)

def main():
  # text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
  # copy_content("static", "public")
  # generate_page("content/index.md", "template.html", "public/index.html")
  generate_pages_recursive("content", "template.html", "public")
  # print(text_node)

def copy_content(source_path, destination_path):
  source_path_exists = os.path.exists(source_path)
  destination_path_exists = os.path.exists(destination_path)

  if not source_path_exists:
    raise Exception(f"Source path {source_path} does not exist")

  if destination_path_exists:
    shutil.rmtree(destination_path)
    
  os.mkdir(destination_path)
  
  for dir in os.listdir(source_path):
    current_path = os.path.join(source_path, dir)
    new_destination_path =  os.path.join(destination_path, dir)
    if os.path.isdir(current_path):
      os.mkdir(new_destination_path)
      copy_content(current_path, new_destination_path)
    elif os.path.isfile(current_path):
      path = shutil.copy(current_path, new_destination_path)
      print(f"file: {current_path} copied to {path}")


main()