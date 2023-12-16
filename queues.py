"""Implementation of Queue"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        temp.next = None
        return temp


# Test Cases
my_queue = Queue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print("Values present in queue:")
my_queue.print_queue()

print("De-queueing value: ", my_queue.dequeue().value)
print("De-queueing next value: ", my_queue.dequeue().value)
print("De-queueing next value: ", my_queue.dequeue().value)
print("De-queueing next value: ", my_queue.dequeue())

