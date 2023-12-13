"""
This file consists the Python Implementation of Doubly Linked List and its various methods.
@author: Mateen Sofi
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print("Node", temp)
            print("Value", temp.value)
            print("Prev", temp.prev)
            print("Next", temp.next)
            print("++++++++++++++++++++++++++++")
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        temp.prev = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = self.head.prev
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        self.length -= 1
        temp.next = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index <= self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - index):
                temp = temp.prev

        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # Case 1 - Index Out of Bounds
        if index < 0 or index > self.length:
            return False

        # Case 2 - Insert at the beginning
        if index == 0:
            return self.prepend(value)

        # Case 3 - Insert at the end
        if index == self.length:
            return self.append(value)

        # General Case
        new_node = Node(value)
        current_node = self.get(index)
        new_node.next = current_node
        new_node.prev = current_node.prev
        current_node.prev = new_node
        new_node.prev.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        before = self.get(index-1)
        temp = before.next
        after = temp.next

        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        return temp


# Create a Doubly Linked List
my_linked_list = DoublyLinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.append(50)
my_linked_list.prepend(0)

my_linked_list.print_list()

# Test Case for Pop
print("Popping the last node")
print(my_linked_list.pop())
print("++++++++++++++++++++++++")

# Test Case for Pop First
print("Popping First Node")
print(my_linked_list.pop_first())
print("++++++++++++++++++++++++")
print("Printing List Again After Popping First Node")
my_linked_list.print_list()

print("Getting value from first half at index = 2")
print(my_linked_list.get(2))

print("Getting value from second half at index = 4")
print(my_linked_list.get(4))

print("Setting value at index = 2")
print(my_linked_list.set(2, 200))
my_linked_list.print_list()

# Test Cases for Insert
print(my_linked_list.insert(2, 250))
my_linked_list.print_list()

# Test Cases for Remove
my_linked_list.print_list()
print("After removing node")
print(my_linked_list.remove(4))
print("LL after node removal")
my_linked_list.print_list()
