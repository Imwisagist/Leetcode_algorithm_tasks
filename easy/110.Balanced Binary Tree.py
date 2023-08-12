# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def height(root):
        if root is None: return 0

        leftheight, rightheight = height(root.left), height(root.right)
        
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1: return -1
        
        return max(leftheight, rightheight) + 1
    
    return height(root) >= 0
    

tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

assert isBalanced(tree1) is True

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(2)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(3)
tree2.left.left.left = TreeNode(4)
tree2.left.left.right = TreeNode(4)

assert isBalanced(tree2) is False
