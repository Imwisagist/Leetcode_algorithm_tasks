# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



def postorder(root: Node) -> List[int]:
    def dfs(node):
        if node:
            for c in node.children: dfs(c)

            res.append(node.val)
    
    res = []; dfs(root)
    
    return res
