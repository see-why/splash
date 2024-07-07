from src.textnode import TextNode

from src.htmlnode import LeafNode

def text_node_to_html_node(text_node):
  match text_node.text_type:
    case TextNode.text_type_text:
      return LeafNode(None, text_node.text)
    case TextNode.text_type_bold:
      return LeafNode("b", text_node.text)
    case TextNode.text_type_italic:
      return LeafNode("i", text_node.text)
    case TextNode.text_type_code:
      return LeafNode("code", text_node.text)
    case TextNode.text_type_link:
      return LeafNode("a", text_node.text, {"href": text_node.url})
    case TextNode.text_type_image:
      return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    case _:
      raise Exception("invalid text")