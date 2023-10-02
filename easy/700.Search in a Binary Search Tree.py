# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root:
        while root:
            if root.val == val: return root

            root = root.left if val < root.val else root.right


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)

searchBST(tree,2)
