# https://leetcode.com/problems/symmetric-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def is_sym(left, right) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return left.val == right.val and is_sym(left.left,right.right) and is_sym(left.right, right.left)
        
    return is_sym(root.left, root.right)


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(4)
tree1.right = TreeNode(2)
tree1.right.left = TreeNode(4)
tree1.right.right = TreeNode(3)

assert isSymmetric(tree1) is True

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.left.right = TreeNode(3)
tree2.right = TreeNode(2)
tree2.right.right = TreeNode(3)

assert isSymmetric(tree2) is False
