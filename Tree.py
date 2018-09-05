class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

  def get_value(self):
    return self.value

  def add_child(self, value):
    new_node = Node(value)
    self.children.append(new_node)

  def get_children(self):
    return self.children

my_node = Node(1)
my_node.add_child(3)
my_node.add_child(7)
my_node.add_child(2)
my_node.add_child(5)

for node in my_node.get_children():
  print('value -> ', node.get_value())
