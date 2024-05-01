# https://leetcode.com/problems/binary-tree-right-side-view/description/
from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    level = defaultdict(int)

    def dfs(node, depth):
        if not node: return
        if depth not in level: level[depth] = node.val

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)

    return list(level.values())
