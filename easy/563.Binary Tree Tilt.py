# https://leetcode.com/problems/binary-tree-tilt/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTilt(root: Optional[TreeNode]) -> int:
    tilt: int = 0

    def calculate_tilt(node):
        if not node: return 0

        nonlocal tilt

        left_sum = calculate_tilt(node.left)
        right_sum = calculate_tilt(node.right)
        tilt += abs(left_sum - right_sum)

        return left_sum + right_sum + node.val

    calculate_tilt(root)

    return tilt


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

assert findTilt(tree1) == 1

tree2 = TreeNode(4)
tree2.left = TreeNode(2)
tree2.right = TreeNode(9)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(5)
tree2.right.right = TreeNode(7)

assert findTilt(tree2) == 15

tree3 = TreeNode(21)
tree3.left = TreeNode(7)
tree3.right = TreeNode(14)
tree3.left.left = TreeNode(1)
tree3.left.right = TreeNode(1)
tree3.left.left.left = TreeNode(3)
tree3.left.left.right = TreeNode(3)
tree3.right.left = TreeNode(2)
tree3.right.right = TreeNode(2)

assert findTilt(tree3) == 9
