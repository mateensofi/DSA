"""This script implements the is_palindrome method for Doubly Linked List."""


from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListPro(DoublyLinkedList):
    def is_palindrome(self):
        front = self.head
        back = self.tail
        for _ in range(self.length//2):
            if front.value == back.value:
                front = front.next
                back = back.prev
            else:
                return False
        return True


my_dll_1 = DoublyLinkedListPro(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome())


my_dll_2 = DoublyLinkedListPro(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome())



