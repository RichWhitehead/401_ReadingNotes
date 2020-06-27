# node class

class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next
    
class LinkedList:
  def __init__(self, head):
    self.head = head
    
  def insert(self, data):
    node = Node(data)
    node.next(self.head)
    self.head = node
    
    