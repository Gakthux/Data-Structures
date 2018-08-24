class Stack:
  def __init__(self):
    self.stack = []

  def size(self):
    return len(self.stack)

  def is_empty(self):
    return self.size() == 0

  def pop(self):
    if self.is_empty():
      return None
    else:
      return self.stack.pop()

  def push(self, value):
    return self.stack.append(value)

  def get_peak(self):
    if self.is_empty():
      return None
    else:
      return self.stack[-1]

my_stack = Stack()

my_stack.push(3)
print(my_stack.get_peak())
my_stack.push(9)
print(my_stack.get_peak())
my_stack.pop()
print(my_stack.get_peak())
my_stack.pop()
print(my_stack.get_peak())