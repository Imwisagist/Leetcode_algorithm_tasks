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
        left, right, node = stack.pop(); m = (left + right) // 2; node.val = nums[m]
        
        if m > left: node.left = TreeNode(); stack.append((left, m, node.left))
        if m+1 < right: node.right = TreeNode(); stack.append((m+1, right, node.right))
            
    return root
