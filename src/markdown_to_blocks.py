def markdown_to_blocks(mark_down):
  stripped_blocks = []
  blocks = mark_down.split("\n\n")
  for block in blocks:
    stripped_block = block.strip()
    if stripped_block:
      stripped_blocks.append(stripped_block)

  return stripped_blocks