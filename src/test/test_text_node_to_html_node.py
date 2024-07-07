import unittest
from src.textnode import TextNode
from src.htmlnode import LeafNode
from src.text_node_to_html_node import ( text_node_to_html_node )


class TestTextNodeToHtmlNode(unittest.TestCase):
  def test_text_node_to_html_node(self):
    node = TextNode("This is a text node", TextNode.text_type_text)
    self.assertEqual(
      text_node_to_html_node(node),
      LeafNode(None, "This is a text node")
    )

  def test_bold_node_to_html_node(self):
    node = TextNode("This is a bold node", TextNode.text_type_bold)
    self.assertEqual(
      text_node_to_html_node(node),
      LeafNode("b", "This is a bold node")
    )

  def test_italic_node_to_html_node(self):
    node = TextNode("This is a italic node", TextNode.text_type_italic)
    self.assertEqual(
      text_node_to_html_node(node),
      LeafNode("i", "This is a italic node")
    )
  
  def test_code_node_to_html_node(self):
    node = TextNode("This is a code node", TextNode.text_type_code)
    self.assertEqual(
      text_node_to_html_node(node),
      LeafNode("code", "This is a code node")
    )

  def test_link_node_to_html_node(self):
    node = TextNode("This is a link node", TextNode.text_type_link, "https://www.boot.dev")
    self.assertEqual(
      text_node_to_html_node(node),
      LeafNode("a", "This is a link node", {'href': 'https://www.boot.dev'})
    )

  def test_image_node_to_html_node(self):
    node = TextNode("https://www.boot.dev/image.jpg", TextNode.text_type_image, "https://www.boot.dev/image.jpg")
    self.assertEqual(
      text_node_to_html_node(node),
      LeafNode("img", "", {'src': 'https://www.boot.dev/image.jpg', 'alt':'https://www.boot.dev/image.jpg'})
    )
  
  def test_invalid_text_type(self):
    def function():
      text_node_to_html_node(TextNode("This is a code node", "invalid"))
    self.assertRaises(
      Exception,
      function
    )



if __name__ == "__main__":
  unittest.main()