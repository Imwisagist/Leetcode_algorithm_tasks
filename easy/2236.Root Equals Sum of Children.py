# https://leetcode.com/problems/root-equals-sum-of-children/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def checkTree(root: Optional[TreeNode]) -> bool:
        
    return root.val == (root.left.val + root.right.val)


tree1 = TreeNode(10)
tree1.left = TreeNode(4)
tree1.right = TreeNode(6)

assert checkTree(tree1) is True

tree2 = TreeNode(5)
tree2.left = TreeNode(3)
tree2.right = TreeNode(1)

assert checkTree(tree2) is False
