# https://leetcode.com/problems/univalued-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isUnivalTree(root: Optional[TreeNode]) -> bool:
    val,stack = root.val,[root]

    while stack:
        node = stack.pop()

        if node.val != val: return False

        if node.left: stack.append(node.left)
        
        if node.right: stack.append(node.right)

    return True


tree = TreeNode(1)
tree.left = TreeNode(1)
tree.right = TreeNode(1)
tree.left.left = TreeNode(1)

assert isUnivalTree(tree) is True

tree2 = TreeNode(2)
tree2.left = TreeNode(2)
tree2.right = TreeNode(2)
tree2.right.right = TreeNode(5)

assert isUnivalTree(tree2) is False
