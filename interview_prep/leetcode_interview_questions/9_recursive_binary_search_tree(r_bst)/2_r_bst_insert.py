
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
        if self.root and self.root.left:
            left = self.root.left.value
        if self.root and self.root.right:
            right = self.root.right.value

        print(f"Root: {root}")
        print(f"Left: {left}")
        print(f"Right: {right}")

        print(f"{'-' * 100}")

    def __r_insert(self, current_node, value):

        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node




    def insert(self, value):
        if self.root is None:
            self.root = Node(value)

        self.__r_insert(self.root, value)
        return True

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
