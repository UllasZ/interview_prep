class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
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


# Instantiate BST
tree = BinarySearchTree()

# insert
tree.insert(1)
tree.insert(-1)
tree.insert(3)

# print BST
tree.print_tree()
