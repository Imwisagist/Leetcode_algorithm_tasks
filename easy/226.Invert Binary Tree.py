# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack: list[TreeNode] = [root]

    while stack:
        node: TreeNode = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right

    return root


tree1 = TreeNode(4)
tree1.left = TreeNode(2)
tree1.right = TreeNode(7)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(3)
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(9)

invertTree(tree1)
