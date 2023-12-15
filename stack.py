"""This file implements the Stack using Linked List"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def peek(self):
        if self.top:
            return self.top.value
        return None


# Test Cases
my_stack = Stack(1)
my_stack.push(2)
my_stack.push(4)
print("Top Node Value: ", my_stack.top.value)
print("Stack Height: ", my_stack.height)

print("Node Popped with value: ", my_stack.pop().value)
print("Stack Height: ", my_stack.height)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

my_stack.push(10)
print("Top Node Value: ", my_stack.top.value)
print("Stack Height: ", my_stack.height)

print("Peeking Stack: ", my_stack.peek())
