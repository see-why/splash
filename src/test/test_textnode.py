import unittest

from src.textnode import TextNode


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    self.assertEqual(node1, node2)

  def test_eq_false_url_none(self):
    node1 = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node1, node2)

  def test_eq_false_different_text(self):
    node1 = TextNode("This is a text node", "bold")
    node2 = TextNode("This is not a text node", "bold")
    self.assertNotEqual(node1, node2)

  def test_eq_false_different_type(self):
    node1 = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "italic")
    self.assertNotEqual(node1, node2)

  def test_repr_false_different_type(self):
    node1 = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "italic")
    self.assertNotEqual(str(node1), str(node2))

  def test_repr_eq_(self):
    node1 = TextNode("This is a text node", "italic")
    node2 = TextNode("This is a text node", "italic")
    self.assertEqual(str(node1), str(node2))

if __name__ == "__main__":
    unittest.main()