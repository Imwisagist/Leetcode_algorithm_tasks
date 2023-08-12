# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: Optional[TreeNode]) -> int:
    if not root: return 0

    if not root.left and not root.right: return 1

    left = minDepth(root.left) if root.left else float('inf')
    right = minDepth(root.right) if root.right else float('inf')

    return 1 + min(left,right)  


tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

assert minDepth(tree1) == 2

tree2 = TreeNode(2)
tree2.right = TreeNode(3)
tree2.right.right = TreeNode(4)
tree2.right.right.right = TreeNode(5)
tree2.right.right.right.right = TreeNode(6)

assert minDepth(tree2) == 5
