import unittest

from src.inline_markdown import (split_nodes_delimiter)

from src.textnode import (
    TextNode
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded", TextNode.text_type_bold),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextNode.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded", TextNode.text_type_bold),
                TextNode(" word and ", TextNode.text_type_text),
                TextNode("another", TextNode.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextNode.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded word", TextNode.text_type_bold),
                TextNode(" and ", TextNode.text_type_text),
                TextNode("another", TextNode.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", TextNode.text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.text_type_text),
                TextNode("italic", TextNode.text_type_italic),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextNode.text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", TextNode.text_type_bold),
                TextNode(" and ", TextNode.text_type_text),
                TextNode("italic", TextNode.text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("code block", TextNode.text_type_code),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )
    
    def test_split_code_italic_bold(self):
        node = TextNode("This `is text with` an *italic block* **bold word**", TextNode.text_type_text)
        code_split_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)
        bold_split_nodes = split_nodes_delimiter(code_split_nodes, "**", TextNode.text_type_bold)
        new_nodes = split_nodes_delimiter(bold_split_nodes, "*", TextNode.text_type_italic)

        self.assertListEqual(
            new_nodes, 
            [
                TextNode("This ", TextNode.text_type_text),
                TextNode("is text with", TextNode.text_type_code),
                TextNode(" an ", TextNode.text_type_text),
                TextNode("italic block", TextNode.text_type_italic),
                TextNode("bold word", TextNode.text_type_bold),
            ]
        )

    def test_split_italic_code_block(self):
        node = TextNode("This is text with a *italic block* `code block` word", TextNode.text_type_text)
        italic_split_nodes = split_nodes_delimiter([node], "*", TextNode.text_type_italic)
        new_nodes = split_nodes_delimiter(italic_split_nodes, "`", TextNode.text_type_code)

        self.assertListEqual(
            new_nodes, 
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("italic block", TextNode.text_type_italic),
                TextNode("code block", TextNode.text_type_code),
                TextNode(" word", TextNode.text_type_text)
            ]
        )

    def test_split_invalid_format(self):
        node = TextNode("This is text with a `code block` word`", TextNode.text_type_text)
        def function():
            split_nodes_delimiter([node], "`", TextNode.text_type_code)

        self.assertRaises(Exception, function)

    def test_split_invalid_text_type(self):
        node = TextNode("An image of the moon", TextNode.text_type_image)
        new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)

        self.assertListEqual(
            new_nodes, 
            [node]
        )


if __name__ == "__main__":
    unittest.main()
