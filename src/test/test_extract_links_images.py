import unittest
from src.inline_markdown import (extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link)
from src.textnode import TextNode


class TestExtractLinesText(unittest.TestCase):
  def test_extract_markdown_images(self):
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    self.assertEqual(
      extract_markdown_images(text),
      [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
    )

  def test_extract_markdown_links(self):
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    self.assertEqual(
      extract_markdown_links(text),
      [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
    )

  def test_split_nodes_image(self):
    node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        TextNode.text_type_text,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      new_nodes,
      [
        TextNode("This is text with an ", TextNode.text_type_text),
        TextNode("image", TextNode.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and another ", TextNode.text_type_text),
        TextNode(
            "second image", TextNode.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
        ),
      ]
    )

  def test_extract_markdown_image(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

  def test_extract_markdown_multiple_links(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
    )
    self.assertListEqual(
        [
            ("link", "https://boot.dev"),
            ("another link", "https://blog.boot.dev"),
        ],
        matches,
    )

  def test_split_nodes_link(self):
    node = TextNode(
        "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        TextNode.text_type_text,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
      new_nodes,
      [
        TextNode("This is text with a ", TextNode.text_type_text),
        TextNode("link", TextNode.text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and another ", TextNode.text_type_text),
        TextNode(
            "second link", TextNode.text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
        ),
      ]
    )

  def test_split_image(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
        TextNode.text_type_text,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextNode.text_type_text),
            TextNode("image", TextNode.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
        ],
        new_nodes,
    )

  def test_split_image_single(self):
    node = TextNode(
        "![image](https://www.example.com/image.png)",
        TextNode.text_type_text,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("image", TextNode.text_type_image, "https://www.example.com/image.png"),
        ],
        new_nodes,
    )

  def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextNode.text_type_text,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextNode.text_type_text),
            TextNode("image", TextNode.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextNode.text_type_text),
            TextNode(
                "second image", TextNode.text_type_image, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

  def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
        TextNode.text_type_text,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextNode.text_type_text),
            TextNode("link", TextNode.text_type_link, "https://boot.dev"),
            TextNode(" and ", TextNode.text_type_text),
            TextNode("another link", TextNode.text_type_link, "https://blog.boot.dev"),
            TextNode(" with text that follows", TextNode.text_type_text),
        ],
        new_nodes,
    )


if __name__ == "__main__":
  unittest.main()