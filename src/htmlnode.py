class HtmlNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def __eq__(self, other):
    return (
      self.tag == other.tag and
      self.value == other.value and 
      self.children == other.children and 
      self.props == other.props
    )

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    if self.props:
      import functools
      return functools.reduce(lambda prefix, suffix :  prefix + f' {suffix[0]}="{suffix[1]}"', self.props.items(), "")
    return None

  def __repr__(self):
    return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
  

class LeafNode(HtmlNode):
  def __init__(self, tag, value, props=None):
    if value == None:
      raise ValueError("Value not set")

    super().__init__(tag, value, None, props)

  def to_html(self):
    props = self.props_to_html() or ""
    return f"<{self.tag}{props}>{self.value}</{self.tag}>" if self.tag else self.value
    

  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"
  

class ParentNode(HtmlNode):
  def __init__(self, tag, children, props=None, value=None):
    super().__init__(tag, value, children, props)

  def to_html(self):
    if self.children == None:
      raise ValueError("Children not set")  
    if self.tag == None:
      raise ValueError("Tag not set")
    
    props = self.props_to_html() or ""
  
    import functools
    return functools.reduce(
      lambda parent, child: parent + f"{child.to_html()}", 
      self.children,
      f"<{self.tag}{props}>"
    ) + f"</{self.tag}>"

  def __repr__(self):
    return f"ParentNode({self.tag}, {self.children}, {self.props})"