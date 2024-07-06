from htmlnode import HtmlNode, LeafNode, ParentNode

class TextNode:
  text_type_bold = "bold"
  text_type_code = "code"
  text_type_image = "image"
  text_type_italic = "italic"
  text_type_link = "link"
  text_type_text = "text"

  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other):
    return (self.text == other.text
             and self.text_type == other.text_type 
             and self.url == other.url)
  
  def text_node_to_html_node(self):
    match self.text:
      case TextNode.text_type_text:
        return LeafNode(None, self.text)
      case TextNode.text_type_bold:
        return LeafNode("b", self.text)
      case TextNode.text_type_italic:
        return LeafNode("i", self.text)
      case TextNode.text_type_code:
        return LeafNode("code", self.text)
      case TextNode.text_type_link:
        return LeafNode("a", self.text, {"href": self.url})
      case TextNode.text_type_image:
        return LeafNode("img", "", {"src": self.url, "alt": self.text})
        

  def __repr__(self):
    return f"TextNode('{self.text}', '{self.text_type}', '{self.url}')"

