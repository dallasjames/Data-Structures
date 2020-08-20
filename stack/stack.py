import sys

sys.path.extend('../singly_linked_list')
from singly_linked_list.singly_linked_list import LinkedList
import array

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   array is more code on this component but easier to work with
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        # self.storage = array.array('i', [])

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        # self.storage.append(value)
        # self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()
        # if len(self.storage) > 0:
        #     popped = self.storage[-1]
        #     self.storage.pop()
        #     self.size -= 1
        #     return popped
        # else:
        #     return None
