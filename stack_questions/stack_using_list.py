"""This scripts implements stacks using python list"""


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.stack_list:
            return self.stack_list.pop()
        return None

    def peek(self):
        if self.stack_list:
            return self.stack_list[-1]
        return None

    def is_empty(self):
        return len(self.stack_list) == 0

    def size(self):
        return len(self.stack_list)

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print("Stack before pop():")
    my_stack.print_stack()

    print("\nPopped node:")
    print(my_stack.pop())

    print("\nStack after pop():")
    my_stack.print_stack()
