# https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluateTree(root: Optional[TreeNode]) -> bool:
    if root.val==3:
        return evaluateTree(root.left) and evaluateTree(root.right)
    elif root.val==2:
        return evaluateTree(root.left) or evaluateTree(root.right)
    
    return root.val
