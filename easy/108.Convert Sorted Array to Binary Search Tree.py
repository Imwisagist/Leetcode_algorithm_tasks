# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    root = TreeNode(); stack = [(0, len(nums), root)]

    while stack:
        i, j, node = stack.pop(); m = (i + j) // 2; node.val = nums[m]
        
        if m > i: node.left = TreeNode(); stack.append((i, m, node.left))
        if m+1 < j: node.right = TreeNode(); stack.append((m+1, j, node.right))
            
    return root
