"""
# Search in a Binary Search Tree

- You are given the root of a binary search tree (BST) and an integer val.
- Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
- If such a node does not exist, return null.

Example 1:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]

Example 2:
    Input: root = [4,2,7,1,3], val = 5
    Output = []
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_bst():
    return TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))


class Solution:
    def search_bst(self, root: Optional[TreeNode], val):

        if root is None:
            return "Value not present in the tree."

        if root.val == val:
            return f"Value {root.val} is present in the tree."
        elif root.val > val:
            return self.search_bst(root.left, val)
        else:
            return self.search_bst(root.right, val)


solution = Solution()
value = 2
result = solution.search_bst(build_bst(), value)
print(result)
