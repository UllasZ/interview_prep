
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

    def min_value(self, current_node):

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value

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

    def __delete_node(self, current_node, value):

        if current_node is None:
            return None

        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)

        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)

        else:

            if current_node.left is None and current_node.right is None:
                return None

            elif current_node.left is None:
                current_node = current_node.right

            elif current_node.right is None:
                current_node = current_node.left

            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

# Instantiate RecursiveBST
tree = RecursiveBST()

# insert
tree.insert(2)
tree.insert(1)
tree.insert(3)


# min_value
print(tree.min_value(tree.root))
print(tree.min_value(tree.root.right))

# print BST
print("\nTree before delete")
tree.print_tree()

tree.delete_node(2)

# print BST
print("\nTree after delete")
tree.print_tree()