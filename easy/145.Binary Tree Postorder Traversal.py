# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    head, stack, result = root, [], []

    while head or stack:
        if head:
            result.append(head.val)
            if head.left:
                stack.append(head.left)
            head = head.right
        else:
            head = stack.pop()

    return result[::-1]


tree1 = TreeNode(5)
tree1.right = TreeNode(6)
tree1.right.right = TreeNode(3)
tree1.right.left = TreeNode(8)
tree1.left = TreeNode(435)

assert postorderTraversal(tree1) == [435, 8, 3, 6, 5]
