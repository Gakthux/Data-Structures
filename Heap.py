import math

class Heap:
  def __init__(self):
    self.heap = []

  def get_heap(self):
    return self.heap

  def size(self):
    return len(self.heap)

  def is_empty(self):
    return self.size() == 0

  def find_max(self):
    return self.heap[0]

  def extract_max(self):
    if self.is_empty():
      return None
    if self.size() == 1:
      return self.heap.pop()
    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    old_max = self.heap.pop()
    # this is the position in the tree of the element we need to move to the right spot
    elem_pos = 1
    left_pos = elem_pos * 2 
    right_pos = elem_pos * 2 + 1
    while (self.size() > left_pos or self.size() > right_pos) and \
          self.heap[elem_pos - 1] < self.heap[left_pos - 1] and \
          self.heap[elem_pos - 1] < self.heap[right_pos - 1]:
      if self.size() < left_pos:
        self.heap[elem_pos - 1], self.heap[left_pos - 1] = self.heap[left_pos - 1], self.heap[elem_pos - 1]
        elem_pos = left_pos
      elif self.size() < right_pos:
        self.heap[elem_pos - 1], self.heap[right_pos - 1] = self.heap[right_pos - 1], self.heap[elem_pos - 1]
        elem_pos = right_pos
      else:
        highest_value_pos = left_pos if self.heap[left_pos - 1] > self.heap[right_pos - 1] else right_pos
        self.heap[elem_pos - 1], self.heap[highest_value_pos - 1] = self.heap[highest_value_pos - 1], self.heap[elem_pos - 1]
        elem_pos = highest_value_pos
        left_pos = elem_pos * 2 
        right_pos = elem_pos * 2 + 1
    return old_max

  def insert(self, value):
    self.heap.append(value)
    # this is the position in the tree of the element we need to move to the right spot
    elem_pos = self.size()
    if elem_pos == 1:
      return value
    parent_pos = math.floor(elem_pos / 2)
    while self.heap[parent_pos - 1] < value and elem_pos != 1:
      # swap elements in List
      self.heap[elem_pos - 1], self.heap[parent_pos - 1] = self.heap[parent_pos - 1], self.heap[elem_pos - 1]
      elem_pos = parent_pos
      parent_pos = math.floor(elem_pos / 2)
    return value

my_heap = Heap()

my_heap.insert(5)
my_heap.insert(1)
my_heap.insert(10)
my_heap.insert(7)
my_heap.insert(5)
my_heap.insert(12)
my_heap.insert(5)
my_heap.insert(1)
my_heap.insert(9)
my_heap.insert(7)
my_heap.insert(8)
print('Heap: ', my_heap.get_heap())
my_heap.extract_max()
print('Heap: ', my_heap.get_heap())
my_heap.extract_max()
print('Heap: ', my_heap.get_heap())
my_heap.extract_max()
print('Heap: ', my_heap.get_heap())
my_heap.extract_max()
print('Heap: ', my_heap.get_heap())