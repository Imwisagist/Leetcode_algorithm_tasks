# https://leetcode.com/problems/sum-of-left-leaves/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    stack, sum = [(root, False)], 0

    while stack:
        node, is_left = stack.pop()
        if node:
            if not node.left and not node.right and is_left:
                sum += node.val
            else:
                stack.append((node.left, True))
                stack.append((node.right, False))

    return sum


tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

assert sumOfLeftLeaves(tree1) == 24

tree2 = TreeNode(1)

assert sumOfLeftLeaves(tree2) == 0
