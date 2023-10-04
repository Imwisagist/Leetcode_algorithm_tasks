# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val; self.children = children


def preorder(root: Node) -> List[int]:
    if root:
        return [root.val] + sum([preorder(n) for n in root.children],[])
