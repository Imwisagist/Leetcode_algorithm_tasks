# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root: Optional[TreeNode], k: int) -> bool:
    stack, values = [root], {}
    
    while stack:
        node = stack.pop()

        if node:
            if node.val in values:
                return True
            
            values[k - node.val] = True
            stack += [node.left]
            stack += [node.right]
        
    return False


tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.right = TreeNode(6)
tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(4)
tree1.right.right = TreeNode(7)

assert findTarget(tree1, 9) is True
assert findTarget(tree1, 28) is False
