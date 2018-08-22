class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def get_value(self):
    return self.value

  def set_next(self, new_next):
    self.next = new_next

  def get_next(self):
    return self.next

class LinkedList:
  def __init__(self):
    self.head = None

  def add_node(self, value):
    new_node = Node(value)
    new_node.set_next(self.head)
    self.head = new_node
    
  def set_head(self, new_head):
    self.head = new_head

  def get_head(self):
    return self.head

  def get_size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.get_next()
    return count

  def search_node(self, value):
    current = self.head
    node_found = False
    while node_found is False and current:
      if (current.get_value() is value):
        node_found = True
      else:
        current = current.get_next()
    if node_found is False:
      return 'Data not in list'
    return current

  def delete_node(self, value):
    current = self.head
    previous = None
    node_found = False
    while node_found is False and current:
      if (current.get_value() is value):
        node_found = True
      else:
        previous = current
        current = current.get_next()
    if (node_found is False):
      return 'No deletable node found'
    if (previous is None):
      self.head = current.get_next()
    else:
      next_node = current.get_next()
      previous.set_next(next_node)