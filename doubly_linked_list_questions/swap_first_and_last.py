"""Given a doubly linked list, swap the values of first and last node. The nodes themselves are not swapped."""


from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListPro(DoublyLinkedList):
    def swap_first_last(self):
        if self.head and self.head != self.tail:
            temp = self.head.value
            self.head.value = self.tail.value
            self.tail.value = temp


linked_list = DoublyLinkedListPro(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("DLL before swap:")
linked_list.print_list()

linked_list.swap_first_last()

print("DLL after swap:")
linked_list.print_list()
