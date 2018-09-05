import numpy as np

class HashTable:
  def __init__(self):
    self.hash_table = {}

  def hash_string(self, string):
    return sum(map(ord,string)) % 2069

  def add_element(self, string):
    hash = self.hash_string(string)
    if hash in self.hash_table:
      self.hash_table[hash].append(string)
    else:
      self.hash_table[hash] = [string]

my_ht = HashTable()

my_ht.add_element('hello')
my_ht.add_element('fun')
my_ht.add_element('charlie')
my_ht.add_element('michel')
my_ht.add_element('cochon')
my_ht.add_element('radis')
my_ht.add_element('test')
my_ht.add_element('poulpe')
my_ht.add_element('grenouille')
my_ht.add_element('truite')
my_ht.add_element('artiste')
my_ht.add_element('a')
my_ht.add_element('b')
my_ht.add_element('c')
my_ht.add_element('d')
my_ht.add_element('e')
my_ht.add_element('f')
my_ht.add_element('g')
my_ht.add_element('h')
my_ht.add_element('i')
my_ht.add_element('j')
my_ht.add_element('k')
my_ht.add_element('l')
my_ht.add_element('m')
my_ht.add_element('n')
my_ht.add_element('o')
my_ht.add_element('p')
my_ht.add_element('q')
my_ht.add_element('r')
my_ht.add_element('s')
my_ht.add_element('t')
my_ht.add_element('tt')
my_ht.add_element('ttt')
my_ht.add_element('u')
my_ht.add_element('v')
my_ht.add_element('w')
my_ht.add_element('x')
my_ht.add_element('y')
my_ht.add_element('z')

print(my_ht.hash_table)
  