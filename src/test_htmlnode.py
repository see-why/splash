import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
  def test_repr(self):
    node2 = HtmlNode("h1", "Son", [], { "class": "roman","id": "foo"})
    node3 = HtmlNode("h2", "Father", [], {"class": "saxon", "id": "foobar"})
    node = HtmlNode("p", "I am maximus", [node2, node3], {"class": "gladiator", "id": "prince"} )

    self.maxDiff = None
    expected_result = ("HtmlNode(p, I am maximus, [HtmlNode(h1, Son, [], {'class': 'roman', 'id': 'foo'}), HtmlNode(h2, Father, [], {'class': 'saxon', 'id': 'foobar'})], {'class': 'gladiator', 'id': 'prince'})")
    self.assertEqual(expected_result, str(node))

  def test_repr_empty_children(self):
    node2 = HtmlNode(None, None, None, None)
    node3 = HtmlNode(None, None, None, None)
    node = HtmlNode("p", "I am maximus", [node2, node3], {"class": "gladiator", "id": "prince"} )

    self.maxDiff = None
    expected_result = ("HtmlNode(p, I am maximus, [HtmlNode(None, None, None, None), HtmlNode(None, None, None, None)], {'class': 'gladiator', 'id': 'prince'})")
    self.assertEqual(expected_result, str(node))

  def test_repr_no_children(self):
    node = HtmlNode("p", "I am maximus", None, {"class": "gladiator", "id": "prince"} )

    self.maxDiff = None
    expected_result = ("HtmlNode(p, I am maximus, None, {'class': 'gladiator', 'id': 'prince'})")
    self.assertEqual(expected_result, str(node))

  def test_props_to_html_with_no_props(self):
    node = HtmlNode("p", "I am maximus", None, None)
    self.assertEqual(None, node.props_to_html())

  def test_leaf_child_no_props_to_html(self):
    leaf = LeafNode("p", "This is a paragraph of text.")
    self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

  def test_leaf_child_to_html(self):
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(leaf2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

  def test_no_value_leaf_child(self):
    leaf = LeafNode("p", None)
    self.assertRaises(ValueError)
  
  def test_leaf_node_repr(self):
    leaf = LeafNode(
      "a", 
      "Don't click me!", {"href": "https://www.google.com"}
    )
    self.assertEqual(
      "LeafNode(a, Don't click me!, {'href': 'https://www.google.com'})",
      str(leaf)
    )
  
  def test_parent_to_html(self):
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    self.assertEqual(
      node.to_html(), 
      "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    )
  
  def test_parent_to_html_with_nested_parents(self):
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ParentNode(
                "div",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        ],
    )

    self.assertEqual(
      node.to_html(), 
      "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div></p>"
    )

  def test_to_html_with_children(self):
      child_node = LeafNode("span", "child")
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>",
      )

if __name__ == "__main__":
  unittest.main()