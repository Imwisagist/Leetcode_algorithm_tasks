# https://leetcode.com/problems/range-sum-of-bst/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right


def rangeSumBST(root: Optional[TreeNode],low: int,high: int) -> int:
    res = 0

    def dfs(node):
        nonlocal res
        if node:
            if node.val > low: dfs(node.left)
            if low <= node.val <= high: res += node.val
            if node.val < high: dfs(node.right)

    dfs(root)

    return res

tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right.right = TreeNode(18)

assert rangeSumBST(tree1,7,15) == 32