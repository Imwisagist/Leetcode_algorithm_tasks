# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, lower, upper):
        if not node: return True

        if lower < node.val < upper:
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        else: return False

    return dfs(root, -float('inf'), float('inf'))


t = TreeNode(5)
t.left = TreeNode(1)
t.right = TreeNode(4)
t.right.right = TreeNode(6)
t.right.left = TreeNode(3)

assert isValidBST(t) is False
