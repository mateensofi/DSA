"""This file implements the remove_duplicates function by extending the LinkedList class.
The duplicate nodes are removed by calling the remove_duplicates function."""
from linkedlist import LinkedList


class RemoveDuplicates(LinkedList):
    def remove_duplicates(self):
        values = set()
        prev = None
        current = self.head
        while current:
            if current.value not in values:
                values.add(current.value)
                prev = current
            else:
                prev.next = current.next
                self.length -= 1
            current = current.next


my_linked_list = RemoveDuplicates(10)
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.append(20)
my_linked_list.append(70)
my_linked_list.append(30)
my_linked_list.append(50)

my_linked_list.print_list()
print("After removing duplicates")
my_linked_list.remove_duplicates()
my_linked_list.print_list()
