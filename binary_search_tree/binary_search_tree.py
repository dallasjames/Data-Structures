"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from stack.stack import Stack
import sys

sys.path.extend('../singly_linked_list')
from singly_linked_list.singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        # self.storage = array.array('i', [])

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        # self.size += 1
        # self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()
        # if len(self.storage) > 0:
        #     dequeued = self.storage[0]
        #     self.size -= 1
        #     self.storage.remove(self.storage[0])
        #     return dequeued
        # else:
        #     return None


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target > self.value:
            if self.right == target:
                return True
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left == target:
                return True
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        new_max = self
        while new_max.right is not None:
            new_max = new_max.right
        return new_max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value is None:
            return None
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        cur_node = self
        queue = Queue()
        queue.enqueue(cur_node)
        while len(queue) > 0:
            cur_node = queue.dequeue()
            print(cur_node.value)
            if cur_node.right is not None:
                queue.enqueue(cur_node.right)
            if cur_node.left is not None:
                queue.enqueue(cur_node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        cur_node = self
        stack = Stack()
        stack.push(cur_node)
        while stack.size > 0:
            cur_node = stack.pop()
            print(cur_node.value)
            if cur_node.right is not None:
                stack.push(cur_node.right)
            if cur_node.left is not None:
                stack.push(cur_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)  # root
#
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()
#
# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
