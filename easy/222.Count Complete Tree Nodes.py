# https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def countNodes(root: Optional[TreeNode]) -> int:
    head, stack, count = root, [], 0

    while head or stack:
        if head:
            count += 1
            stack.append(head.right)
            head = head.left
        else:
            head = stack.pop()

    return count


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.right.left = TreeNode(6)

assert countNodes(tree1) == 6

tree2 = []

assert countNodes(tree2) == 0

tree3 = TreeNode(1)

assert countNodes(tree3) == 1
