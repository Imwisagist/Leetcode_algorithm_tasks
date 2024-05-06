# https://leetcode.com/problems/find-duplicate-subtrees/description/
from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDuplicateSubtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    d, res = defaultdict(int), []

    def _preorder(node):
        if not node: return "NULL"

        subtree = ",".join([str(node.val), _preorder(node.left), _preorder(node.right)])

        if d[subtree] == 1: res.append(node)

        d[subtree] += 1

        return subtree

    _preorder(root)

    return res
