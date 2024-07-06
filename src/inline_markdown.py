from textnode import TextNode

  # work on nested examples later  
def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextNode.text_type_text:
      new_nodes.append(node)
      continue
    split_nodes = []
    sub_texts = node.text.split(delimiter)

    if len(sub_texts) % 2 == 0:
      raise Exception("invalid markdown, add missing closing formatter")

    for idx in range(len(sub_texts)):
      if sub_texts[idx] == "" or sub_texts[idx] == " ":
        continue
      if idx % 2 == 0:
        split_nodes.append(TextNode(sub_texts[idx], TextNode.text_type_text))
      else:
        split_nodes.append(TextNode(sub_texts[idx], text_type))

    new_nodes.extend(split_nodes)

  return new_nodes