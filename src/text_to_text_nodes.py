from src.inline_markdown import (
  split_nodes_delimiter,
  split_nodes_link,
  split_nodes_image,
)

from src.textnode import TextNode

def text_to_text_nodes(text):
  node = TextNode(text, TextNode.text_type_text, TextNode)
  image_split_nodes = split_nodes_image([node])
  link_split_nodes = split_nodes_link(image_split_nodes)
  bold_split_nodes = split_nodes_delimiter(link_split_nodes, "**", TextNode.text_type_bold)
  italic_split_nodes = split_nodes_delimiter(bold_split_nodes, "*", TextNode.text_type_italic)
  final_text_nodes = split_nodes_delimiter(italic_split_nodes, "`", TextNode.text_type_code)

  return final_text_nodes
