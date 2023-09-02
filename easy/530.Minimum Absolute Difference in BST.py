# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    cur, stack, min_diff, prev_val = root, [], float('inf'), -float('inf')

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        node: TreeNode = stack.pop()
        min_diff = min(min_diff, abs(node.val - prev_val))
        prev_val = node.val
        cur = node.right

    return min_diff


tree1 = TreeNode(4)
tree1.left = TreeNode(2)
tree1.right = TreeNode(6)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(3)

assert getMinimumDifference(tree1) == 1

tree2 = TreeNode(1)
tree2.left = TreeNode(0)
tree2.right = TreeNode(48)
tree2.right.left = TreeNode(12)
tree2.right.right = TreeNode(49)

assert getMinimumDifference(tree2) == 1

tree3 = TreeNode(5)
tree3.left = TreeNode(4)
tree3.right = TreeNode(7)

assert getMinimumDifference(tree3) == 1
