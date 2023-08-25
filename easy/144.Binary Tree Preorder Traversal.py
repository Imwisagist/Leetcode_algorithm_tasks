# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    head, stack, result = root, [], []

    while head or stack:
        if head:
            result.append(head.val)
            if head.right:
                stack.append(head.right)
            head = head.left
        else:
            head = stack.pop()

    return result


tree1 = TreeNode(1)
tree1.left = TreeNode(4)
tree1.right = TreeNode(6)
tree1.left.left = TreeNode(10)
tree1.left.right = TreeNode(354)
tree1.right.left = TreeNode(46)
tree1.right.right = TreeNode(23)

assert preorderTraversal(tree1) == [1, 4, 10, 354, 6, 46, 23]
