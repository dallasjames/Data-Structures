class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def __str__(self):
        pass

    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length = self.length - 1
            return current_head.value

    def remove_tail(self):
        if not self.tail:
            return None
        elif self.head == self.tail:
            current_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return current_tail.value
        else:
            new_tail = self.head
            old_tail = self.tail
            while new_tail.next is not self.tail:
                new_tail = new_tail.next
            self.tail = new_tail
            self.length -= 1
            return old_tail.value

    def add_to_head(self, value):
        if not self.head:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = Node(value, self.head)
            self.head = new_node
            self.length += 1

    def remove_at_index(self, index):
        if index >= self.length:
            return None
        elif index == self.lenth:
            self.remove_tail()
        elif index == 0:
            self.remove_head()
        elif self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return target.value
        else:
            prev_node = self.head
            for i in range(index - 1):
                prev_node = prev_node.next
            target = prev_node.next
            prev_node.next = target.next
            target.next = None
            self.length -= 1
            return target.value
