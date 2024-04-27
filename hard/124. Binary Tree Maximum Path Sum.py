# https://leetcode.com/problems/binary-tree-maximum-path-sum/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    res = root.val

    def dfs(root):
        nonlocal res

        if not root: return 0

        l, r = max(dfs(root.left), 0), max(dfs(root.right), 0)
        res = max(res, root.val + l + r)

        return root.val + max(l, r)

    dfs(root)

    return res
