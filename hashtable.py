"""
This file consists of the Python Implementation of Hash Table and its various methods.
@author: Mateen Sofi
"""


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value + ord(char) * 23) % len(self.data_map)
        return hash_value

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys


# For Testing Purposes
hash_table = HashTable()
print("Hash Table before inserting any element")
hash_table.print_table()

print("Hash Table after insertions")
hash_table.set_item("apple", 20)
hash_table.set_item("pear", 40)
hash_table.set_item("banana", 90)
hash_table.set_item("mango", 115)
hash_table.set_item("orange", 70)
hash_table.set_item("grapes", 25)
hash_table.print_table()

print("Getting Items from Hash Table")
print(hash_table.get_item("apple"))
print(hash_table.get_item("grapes"))
print(hash_table.get_item("guava"))

print("Getting all the keys of Hash Table")
print(hash_table.keys())

