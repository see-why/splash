import unittest

from src.text_to_text_nodes import text_to_text_nodes
from src.textnode import TextNode


class TestTextToTextNodes(unittest.TestCase):
  def test_text_to_text_nodes(self):
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    text_nodes = text_to_text_nodes(text)

    self.maxDiff = None

    self.assertListEqual(
      text_nodes,
      [
        TextNode("This is ", TextNode.text_type_text),
        TextNode("text", TextNode.text_type_bold),
        TextNode(" with an ", TextNode.text_type_text),
        TextNode("italic", TextNode.text_type_italic),
        TextNode(" word and a ", TextNode.text_type_text),
        TextNode("code block", TextNode.text_type_code),
        TextNode(" and an ", TextNode.text_type_text),
        TextNode("image", TextNode.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and a ", TextNode.text_type_text),
        TextNode("link", TextNode.text_type_link, "https://boot.dev"),
      ]
    )

if __name__ == "__main__":
  unittest.main()