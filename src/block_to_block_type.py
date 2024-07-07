import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def block_to_block_type(block):
  lines = block.split('\n')
  if re.findall(r'^[#]+ ', block):
    return block_type_heading
  elif re.findall(r'^(```)(.|\n)+(```)$', block):
    return block_type_code
  elif is_character_in_all_lines(r'[>]', lines):
    return block_type_quote
  elif is_character_in_all_lines(r'[*|-] ', lines):
    return block_type_unordered_list
  # elif is_character_in_all_lines(r'[\d]+. ', lines):
  elif is_number_increasing_by_1(lines):
    return block_type_ordered_list
  else:
    return block_type_paragraph

def is_character_in_all_lines(character_exp, lines):
  for line in lines:
    if re.findall(r'^' + character_exp, line) == []:
      return False
  return True

def is_number_increasing_by_1(lines):
  for i in range(len(lines)):
    if not lines[i].startswith(f"{i + 1}. "):
      return False
  return True




