class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        print(f"\n{'-' * 100}")
        print(f"Root: {self.root}")
        print(f"{'-' * 100}")


# Instantiate BST
tree = BinarySearchTree()

# print BST
tree.print_tree()
