"""
Given a linked list, we have to find the kth node from end.
This file uses the predefined LinkedList class and implements a standalone function that takes
linked list and a number "k" as input and returns the kth node"""
from linkedlist import LinkedList

my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.append(50)


def find_kth_node_from_end(linked_list, k):
    slow = linked_list.head
    fast = linked_list.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


# Test Cases
print(find_kth_node_from_end(my_linked_list, 1).value)
print(find_kth_node_from_end(my_linked_list, 5).value)
print(find_kth_node_from_end(my_linked_list, 6))
