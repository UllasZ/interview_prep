class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        print("\n" + "-" * 100)
        print("Hash Table: ")
        for i, value in enumerate(self.data_map):
            print(f"\t{i} : {value}")
        print("-" * 100)

    def set_item(self, key, value):

        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []

        self.data_map[index].append([key, value])


# Instantiate HashTable
hash_table = HashTable()

# set_item
hash_table.set_item("bolts", 2000)
hash_table.set_item("washers", 50)
hash_table.set_item("lumber", 50)

# print_table
hash_table.print_table()
