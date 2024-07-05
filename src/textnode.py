from htmlnode import HtmlNode, LeafNode, ParentNode

class TextNode:
  text_type_code = 
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
      case "text":
        return LeafNode(None, self.text)
      case "bold":
        return LeafNode("b", self.text)
      case "italic":
        return LeafNode("i", self.text)
      case "code":
        return LeafNode("code", self.text)
      case "link":
        return LeafNode("a", self.text, {"href": self.url})
      case "image":
        return LeafNode("img", "", {"src": self.url, "alt": self.text})
      
  def split_nodes_delimiter(old_nodes, delimiter, text_type):

      
  
  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"
