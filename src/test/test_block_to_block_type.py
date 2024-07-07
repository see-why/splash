import unittest

from src.block_to_block_type import (
   block_to_block_type,
   block_type_code,
   block_type_heading,
   block_type_quote,
   block_type_paragraph,
   block_type_ordered_list,
   block_type_unordered_list,
)

class TestBlockToBlockType(unittest.TestCase):
  def test_block_to_block_types(self):
      block = "# heading"
      self.assertEqual(block_to_block_type(block), block_type_heading)
      block = "```\ncode\n```"
      self.assertEqual(block_to_block_type(block), block_type_code)
      block = "> quote\n> more quote"
      self.assertEqual(block_to_block_type(block), block_type_quote)
      block = "* list\n* items"
      self.assertEqual(block_to_block_type(block), block_type_unordered_list)
      block = "1. list\n2. items"
      self.assertEqual(block_to_block_type(block), block_type_ordered_list)
      block = "paragraph"
      self.assertEqual(block_to_block_type(block), block_type_paragraph)




if __name__ == "__main__":
  unittest.main()