# https://leetcode.com/problems/merge-two-binary-trees/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 or not root2: return root2 or root1

    res = TreeNode(root1.val + root2.val)
    res.left = mergeTrees(root1.left, root2.left)
    res.right = mergeTrees(root1.right, root2.right)

    return res


tree = TreeNode(1)
tree.left = TreeNode(3)
tree.right = TreeNode(2)
tree.left.left = TreeNode(5)

tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.right = TreeNode(7)

mergeTrees(tree,tree2)
