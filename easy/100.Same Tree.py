# https://leetcode.com/problems/same-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right, q.right)


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

assert isSameTree(tree1, tree2) is True

tree3 = TreeNode(1)
tree3.left = TreeNode(2)

tree4 = TreeNode(1)
tree4.left = TreeNode(None)
tree4.right = TreeNode(2)

assert isSameTree(tree3, tree4) is False

tree5 = TreeNode(1)
tree5.left = TreeNode(2)
tree5.right = TreeNode(1)

tree6 = TreeNode(1)
tree6.left = TreeNode(1)
tree6.right = TreeNode(2)

assert isSameTree(tree5, tree6) is False
