import os
from pathlib import Path
from src.markdown_to_html_node import markdown_to_html_node
from src.inline_markdown import extract_tite

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  content = read_file(from_path)
  template = read_file(template_path)
  html = markdown_to_html_node(content).to_html()
  title = extract_tite(content).strip()
  title_replaced_template = template.replace("{{ Title }}", title)
  new_html = title_replaced_template.replace("{{ Content }}", html)

  dir = os.path.dirname(dest_path)
  if not os.path.exists(dir):
    os.makedirs(dir)
  
  write_file(dest_path, new_html)
  print(f"Done generating page from {from_path} to {dest_path} using {template_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  for dir in os.listdir(dir_path_content):
    current_path = os.path.join(dir_path_content, dir)
    new_destination_path =  os.path.join(dest_dir_path, dir)
    if os.path.isdir(current_path):
      if not os.path.exists(new_destination_path):
        os.mkdir(new_destination_path)
      generate_pages_recursive(current_path, template_path, new_destination_path)
    elif os.path.isfile(current_path):
      html_path = Path(new_destination_path).with_suffix(".html")
      generate_page(current_path, template_path, html_path)
  
  
def write_file(dest_path, template):
  with open(dest_path, "w") as f:
    f.write(template)

def read_file(path):
  file = open(path, 'r')
  content = file.read()
  file.close()
  return content