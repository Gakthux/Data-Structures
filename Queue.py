class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def get_back(self):
      if self.is_empty():
        return None
      else:
        return self.queue[0]

    def get_front(self):
      if self.is_empty():
        return None
      else:
        return self.queue[-1]

my_queue = Queue()

my_queue.enqueue(3)
print('back: ', my_queue.get_back())
print('front: ', my_queue.get_front())
my_queue.enqueue(9)
print('back: ', my_queue.get_back())
print('front: ', my_queue.get_front())
my_queue.enqueue(15)
print('back: ', my_queue.get_back())
print('front: ', my_queue.get_front())
my_queue.dequeue()
print('back: ', my_queue.get_back())
print('front: ', my_queue.get_front())
my_queue.dequeue()
print('back: ', my_queue.get_back())
print('front: ', my_queue.get_front())