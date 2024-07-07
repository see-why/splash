import re
from src.textnode import TextNode

  # work on nested examples later  
def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextNode.text_type_text:
      new_nodes.append(node)
      continue
    split_nodes = []
    sub_texts = node.text.split(delimiter)

    if len(sub_texts) % 2 == 0:
      raise Exception("invalid markdown, add missing closing formatter")

    for idx in range(len(sub_texts)):
      if sub_texts[idx] == "" or sub_texts[idx] == " ":
        continue
      if idx % 2 == 0:
        split_nodes.append(TextNode(sub_texts[idx], TextNode.text_type_text))
      else:
        split_nodes.append(TextNode(sub_texts[idx], text_type))

    new_nodes.extend(split_nodes)

  return new_nodes

def extract_markdown_images(text):
  return re.findall(r'!\[(.*?)\]\((.*?)\)', text)

def extract_markdown_links(text):
  return re.findall(r'\[(.*?)\]\((.*?)\)', text)

def split_nodes_link(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextNode.text_type_text:
      new_nodes.append(node)
      continue
    link_tuples = extract_markdown_links(node.text)
    text = node.text
    for link_tuple in link_tuples:
      split_nodes = text.split(f"[{link_tuple[0]}]({link_tuple[1]})", 1)
      if split_nodes[0]:
        new_nodes.append(TextNode(split_nodes[0], TextNode.text_type_text))
      new_nodes.append(TextNode(link_tuple[0], TextNode.text_type_link, link_tuple[1]))
      text = split_nodes[1]

    if text:
      new_nodes.append(TextNode(text, TextNode.text_type_text))

  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextNode.text_type_text:
      new_nodes.append(node)
      continue
    image_tuples = extract_markdown_images(node.text)
    text = node.text
    for image_tuple in image_tuples:
      split_nodes = text.split(f"![{image_tuple[0]}]({image_tuple[1]})", 1)
      if split_nodes[0]:
        new_nodes.append(TextNode(split_nodes[0], TextNode.text_type_text))
      new_nodes.append(TextNode(image_tuple[0], TextNode.text_type_image, image_tuple[1]))
      text = split_nodes[1]

    if text:
      new_nodes.append(TextNode(text, TextNode.text_type_text))
    
  return new_nodes
