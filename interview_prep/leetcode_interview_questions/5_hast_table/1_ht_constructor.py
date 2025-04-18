class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = my_hash + ord(letter * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        print("\n" + "-" * 100)
        print("Hash Table: ")
        for i, value in enumerate(self.data_map):
            print(f"\t{i} : {value}")
        print("-" * 100)


# Instantiate HashTable
hash_table = HashTable()

# print_table
hash_table.print_table()
