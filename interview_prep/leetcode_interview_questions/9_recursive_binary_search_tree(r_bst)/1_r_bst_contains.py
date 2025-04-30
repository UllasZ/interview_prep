
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RecursiveBST:
    def __init__(self):
        self.root = None

    def print_tree(self):

        root = None
        left = None
        right = None

        print(f"\n{'-' * 100}")
        if self.root:
            root = self.root.value
        if self.root.left:
            left = self.root.left.value
        if self.root.right:
            right = self.root.right.value

        print(f"Root: {root}")
        print(f"Left: {left}")
        print(f"Right: {right}")

        print(f"{'-' * 100}")

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if new_node.value == temp.value:
                print(False)
                return False

            if new_node.value < temp.value:

                if temp.left is None:
                    temp.left = new_node
                    return True

                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return True

                temp = temp.right


    def __r_contains(self, current_node, value):
        if current_node is None:
            return False

        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def contains(self, value):
        return self.__r_contains(self.root, value)

# Instantiate RecursiveBST
tree = RecursiveBST()

# insert
tree.insert(40)
tree.insert(27)
tree.insert(36)
tree.insert(76)
tree.insert(16)

# print BST
tree.print_tree()

# contains
input_value = 16
result = tree.contains(input_value)
if result:
    print(f"Tree Contains: {input_value}")
else:
    print(f"Tree doesn't not contain {input_value}")
