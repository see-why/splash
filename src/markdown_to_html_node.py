from src.markdown_to_blocks import (markdown_to_blocks)
from src.block_to_block_type import (
  block_to_block_type,
  block_type_paragraph,
  block_type_heading,
  block_type_code,
  block_type_quote,
  block_type_unordered_list,
  block_type_ordered_list
)
from src.text_to_text_nodes import (text_to_text_nodes)
from src.text_node_to_html_node import (text_node_to_html_node)
from src.htmlnode import (ParentNode)


def paragraph_block_inline_markdown_to_html_nodes(block):
  lines = block.split("\n")
  chidldren = []
  for ind, line in enumerate(lines):
    text_nodes = text_to_text_nodes(line) if ind == 0 else text_to_text_nodes(f" {line}")
    child_nodes = [text_node_to_html_node(node) for node in text_nodes]
    chidldren.extend(child_nodes)
  return chidldren

def heading_block_inline_markdown_to_html_nodes(block):
  each_item = block.split(" ")
  text_nodes = text_to_text_nodes(" ".join(each_item[1:]))
  return [text_node_to_html_node(node) for node in text_nodes]

def heading_block_html_tag(block):
  lines = block.split(" ")
  count = len(lines[0])
  return f"h{count}" 

def code_block_inline_markdown_to_html_nodes(block):
  lines = block.split("\n")
  chidldren = []
  for line in lines:
    text_nodes = text_to_text_nodes(line)
    child_nodes = [text_node_to_html_node(node) for node in text_nodes]
    chidldren.extend(child_nodes)
  return chidldren

def quote_block_inline_markdown_to_html_nodes(block):
  lines = block.split("\n")
  chidldren = []
  for ind, line in enumerate(lines):
    each_item = [ item for item in line.split(" ") if item ]
    new_text = " ".join(each_item[1:])
    text_nodes = text_to_text_nodes(new_text) if ind == 0 else text_to_text_nodes(f" {new_text}")
    child_nodes = [text_node_to_html_node(node) for node in text_nodes]
    chidldren.extend(child_nodes)
  return chidldren

def unordered_block_inline_markdown_to_html_nodes(block):
  lines = block.split("\n")
  chidldren = []
  for line in lines:
    text_nodes = text_to_text_nodes(line[2:])
    child_nodes = [text_node_to_html_node(node) for node in text_nodes]
    parent_node = ParentNode("li", child_nodes)
    chidldren.append(parent_node)
  return chidldren

def ordered_block_inline_markdown_to_html_nodes(block):
  lines = block.split("\n")
  chidldren = []
  for line in lines:
    each_item = [ item for item in line.split(" ") if item ]
    text_nodes = text_to_text_nodes(" ".join(each_item[1:]))
    child_nodes = [text_node_to_html_node(node) for node in text_nodes]
    parent_node = ParentNode("li", child_nodes)
    chidldren.append(parent_node)
  return chidldren

def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  html_node = ParentNode("div", [])
  for block in blocks:
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
      children = paragraph_block_inline_markdown_to_html_nodes(block)
      parent = ParentNode("p", children)
      html_node.children.append(parent)
    elif block_type == block_type_heading:
      h_tag = heading_block_html_tag(block)
      children = heading_block_inline_markdown_to_html_nodes(block)
      parent = ParentNode(h_tag, children)
      html_node.children.append(parent)
    # Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.
    elif block_type == block_type_code:
      children = code_block_inline_markdown_to_html_nodes(block)
      parent = ParentNode("code", children)
      grand_parent = ParentNode("pre", [parent])
      html_node.children.append(grand_parent)
    # Quote blocks should be surrounded by a <blockquote> tag.
    elif block_type == block_type_quote:
      children = quote_block_inline_markdown_to_html_nodes(block)
      parent = ParentNode("blockquote", children)
      html_node.children.append(parent)
    # Unordered list blocks should be surrounded by a <ul> tag, and 
    # each list item should be surrounded by a <li> tag.
    elif block_type == block_type_unordered_list:
      children = unordered_block_inline_markdown_to_html_nodes(block)
      parent = ParentNode("ul", children)
      html_node.children.append(parent)
    # Ordered list blocks should be surrounded by a <ol> tag, and 
    # each list item should be surrounded by a <li> tag.
    elif block_type == block_type_ordered_list:
      children = ordered_block_inline_markdown_to_html_nodes(block)
      parent = ParentNode("ol", children)
      html_node.children.append(parent)
  return html_node



