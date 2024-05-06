"""This script implements the reverse method for Doubly Linked List"""

from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListPro(DoublyLinkedList):
    def reverse(self):
        if self.head and self.head != self.tail:
            self.head, self.tail = self.tail, self.head
            temp = self.head
            while temp:
                temp.next, temp.prev = temp.prev, temp.next
                temp = temp.next


linkedlist = DoublyLinkedListPro(10)
linkedlist.append(20)
linkedlist.append(30)

print("Before Reverse...")
linkedlist.print_list()

linkedlist.reverse()
print("After Reverse...")
linkedlist.print_list()
