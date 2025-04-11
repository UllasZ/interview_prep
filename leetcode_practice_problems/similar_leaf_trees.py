"""
# Leaf-Similar Trees

- Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
- For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
- Two binary trees are considered leaf-similar if their leaf value sequence is the same.
- Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true

Example 2:
    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false

Constraints:
    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_bst1():
    return TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))


def build_bst2():
    return TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def collect_leafs(root, values):
            if not root:
                return
            if not root.left and not root.right:
                values.append(root.val)

            collect_leafs(root.left, values)
            collect_leafs(root.right, values)

        leaf_values1, leaf_values2 = [], []

        collect_leafs(root1, leaf_values1)
        collect_leafs(root2, leaf_values2)

        return leaf_values1 == leaf_values2


solution = Solution()
result = solution.leafSimilar(build_bst1(), build_bst2())
print(result)
