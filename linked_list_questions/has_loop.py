"""
Given a linked list, we have to find whether there's a loop/cycle present in the linked list or not.
The approach uses Floyd's Cycle Finding Algorithm (aka Tortoise and Hare Algorithm) to detct the loop.
"""
from linkedlist import LinkedList


class LinkedListPro(LinkedList):
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


my_linked_list_1 = LinkedListPro(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop())  # Returns True


my_linked_list_2 = LinkedListPro(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())  # Returns False
