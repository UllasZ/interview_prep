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

    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []

        # for i in range(len(self.data_map)):
        #     if self.data_map[i] is not None:
        #         for j in range(len(self.data_map[i])):
        #             all_keys.append(self.data_map[i][j][0])

        for i in self.data_map:
            if i is not None:
                for j in i:
                    all_keys.append(j[0])

        print(f"All Keys: {all_keys}")
        return all_keys


# Instantiate HashTable
hash_table = HashTable()

# set_item
hash_table.set_item("bolts", 2000)
hash_table.set_item("washers", 50)
hash_table.set_item("lumber", 50)

# get_item
# print("-" * 100)
# print(f'Value: {hash_table.get_item("bolts")}')
# print(f'Value: {hash_table.get_item("washers")}')
# print(f'Value: {hash_table.get_item("lumber")}')
# print(f'Value: {hash_table.get_item("lumbers")}')

# keys
hash_table.keys()

# print_table
hash_table.print_table()
