"""
This file consists the Python Implementation of LinkedList and its various methods.
@author: Mateen Sofi
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = temp
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        pre = self.get(index-1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # after = temp.next - This line is not required
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


if __name__ == "__main__":
    # Creating the LL
    print("Creating a linked list with node value - 10")
    my_linked_list = LinkedList(10)
    print("Printing after creating")
    my_linked_list.print_list()

    # Reversing the Linked List
    print("Reversing the LL")
    my_linked_list.reverse()
    print("Printing after reversing")
    my_linked_list.print_list()

    # Appending to LL
    print("Appending a node with value - 20")
    my_linked_list.append(20)
    print("Printing after appending")
    my_linked_list.print_list()

    print("Appending a node with value - 30")
    my_linked_list.append(30)
    print("Printing after appending")
    my_linked_list.print_list()

    # Get the value at index i
    print("Getting the node at index 2")
    node = my_linked_list.get(2)
    print("Value of the node at index 2: ", node.value)

    # Get the value at index i
    print("Getting the node at index out of range")
    node = my_linked_list.get(6)
    print("Value of the node at index 6: ", node)

    # Popping from LL
    print("Popping from the linked list")
    popped_node = my_linked_list.pop()
    print("Popped Node", popped_node)
    print("Printing after popping")
    my_linked_list.print_list()

    print("Popping from the linked list")
    popped_node = my_linked_list.pop()
    print("Popped Node", popped_node)
    print("Printing after popping")
    my_linked_list.print_list()

    print("Popping from the linked list")
    popped_node = my_linked_list.pop()
    print("Popped Node", popped_node)
    print("Printing after popping")
    my_linked_list.print_list()

    # Reversing the Linked List
    print("Reversing the LL")
    my_linked_list.reverse()
    print("Printing after reversing")
    my_linked_list.print_list()

    # Prepending to LL
    print("Prepending the value 25 to linked list")
    my_linked_list.prepend(25)
    print("After prepending")
    my_linked_list.print_list()

    # Popping first from LL
    print("Popping first from the linked list")
    popped_node = my_linked_list.pop_first()
    print("Popped Node", popped_node)
    print("Printing after popping")
    my_linked_list.print_list()

    # Popping first from LL
    print("Popping first from the linked list")
    popped_node = my_linked_list.pop_first()
    print("Popped Node", popped_node)
    print("Printing after popping")
    my_linked_list.print_list()

    # Insert into LL
    print("Inserting at index 0")
    my_linked_list.insert(0, 10)
    print("Printing after inserting")
    my_linked_list.print_list()

    # Insert into LL
    print("Inserting at index 1")
    my_linked_list.insert(1, 25)
    print("Printing after inserting")
    my_linked_list.print_list()

    # Insert into LL
    print("Inserting at index 0")
    my_linked_list.insert(0, 52)
    print("Printing after inserting")
    my_linked_list.print_list()

    # Reversing the Linked List
    print("Reversing the LL")
    my_linked_list.reverse()
    print("Printing after reversing")
    my_linked_list.print_list()
