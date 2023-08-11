# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    stack, result = [[root, 1]], 0

    while stack:
        node, depth = stack.pop()

        if node:
            result = max(result, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
        
    return result


tree1 = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)
assert maxDepth(tree1) == 3

tree2 = TreeNode(1)
tree2.right = TreeNode(2)

assert maxDepth(tree2) == 2
