# https://leetcode.com/problems/binary-tree-paths/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    stack, res = [(root, "")], []

    while stack:
        node, path = stack.pop()
        if not (node.left or node.right):
            res.append(path + str(node.val))
        if node.left:
            stack.append((node.left, path + str(node.val) + "->"))
        if node.right:
            stack.append((node.right, path + str(node.val) + "->"))
    
    return res


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.right = TreeNode(5)

assert binaryTreePaths(tree1) == ["1->3", "1->2->5"]
