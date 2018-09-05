class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def get_value(self):
    return self.value

  def get_left(self):
    return self.left

  def get_right(self):
    return self.right

  def set_left(self, value):
    self.left = Node(value)
    return value

  def set_right(self, value):
    self.right = Node(value)
    return value

  def insert(self, value):
    current_value = self.get_value()
    if (value == current_value):
      return value
    elif (value < current_value):
      left_node = self.get_left()
      if (left_node != None):
        left_node.insert(value)
      else:
        return self.set_left(value)
    else:
      right_node = self.get_right()
      if (right_node != None):
        right_node.insert(value)
      else:
        return self.set_right(value)

  def print(self):
    left_node = self.get_left()
    if (left_node != None):
      left_node.print()
    print(self.get_value())
    right_node = self.get_right()
    if (right_node != None):
      right_node.print()

root_node = Node(15)

root_node.insert(2)
root_node.insert(12)
root_node.insert(9)
root_node.insert(23)
root_node.insert(11)
root_node.insert(6)
root_node.insert(16)
root_node.insert(28)
root_node.insert(1)
root_node.insert(22)
root_node.insert(30)

root_node.print()