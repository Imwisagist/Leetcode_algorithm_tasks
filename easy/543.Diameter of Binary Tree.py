# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter: int = 0
    
    def height(root):
        nonlocal diameter
        if not root: return 0
        
        left = height(root.left)
        right = height(root.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1
    
    height(root)

    return diameter


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)

assert diameterOfBinaryTree(tree1)
