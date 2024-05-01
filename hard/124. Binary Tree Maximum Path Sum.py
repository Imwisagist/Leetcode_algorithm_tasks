# https://leetcode.com/problems/binary-tree-maximum-path-sum/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    res = root.val

    def dfs(node):
        nonlocal res

        if not node: return 0

        l, r = max(dfs(node.left), 0), max(dfs(node.right), 0)
        res = max(res, node.val + l + r)

        return node.val + max(l, r)

    dfs(root)

    return res

