"""Given a linked list, we have to remove its kth node from end"""

from linkedlist import LinkedList
from linkedlist import Node


def remove_kth_node_from_end(linked_list, k):
    before = Node(0)
    before.next = linked_list.head
    slow = linked_list.head
    fast = linked_list.head

    for _ in range(k):
        fast = fast.next

    while fast is not None:
        before = before.next
        slow = slow.next
        fast = fast.next

    # Edge Case - When element has to be removed from
    # start of the list, then head needs to be changed
    if k == linked_list.length:
        linked_list.head = slow.next
    else:
        before.next = slow.next

    slow.next = None
    linked_list.length -= 1

    return linked_list.head


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

returned_value = remove_kth_node_from_end(my_linked_list, k=1)
print(returned_value.value)