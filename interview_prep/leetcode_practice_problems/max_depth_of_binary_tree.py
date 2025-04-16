"""
# Maximum Depth of Binary Tree

- Given the root of a binary tree, return its maximum depth.
- A binary tree's maximum depth is the number of nodes along
  the longest path from the root node down to the farthest leaf node.

Example 2:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_bst():
    return TreeNode(3, TreeNode(9, TreeNode(20), TreeNode(-1)), TreeNode(-1))


class Solution:
    def max_depth(self, root: Optional[TreeNode]):

        if root is None:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return max(left, right) + 1


solution = Solution()
result = solution.max_depth(build_bst())
print(result)
