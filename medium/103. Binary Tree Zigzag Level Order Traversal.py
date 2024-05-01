# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []

    q, res = [(root, 0)], []

    while q:
        n, lvl = q.pop()

        if lvl == len(res): res.append([])
        if lvl % 2: res[lvl].append(n.val)
        else: res[lvl].insert(0, n.val)
        if n.left: q.append((n.left, lvl + 1))
        if n.right: q.append((n.right, lvl + 1))

    return res
