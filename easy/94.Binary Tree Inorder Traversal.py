# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result: list = []

    def traversal_nodes(root: Optional[TreeNode]):
        if root:
            traversal_nodes(root.left)
            result.append(root.val)
            traversal_nodes(root.right)

    traversal_nodes(root)

    return result

root = dummy = TreeNode(1)
root.right = TreeNode(2)
root = root.right
root.left = TreeNode(3)

root2 = dummy2 = TreeNode(1)

assert inorderTraversal(dummy) == [1, 3, 2]
assert inorderTraversal(dummy2) == [1]
