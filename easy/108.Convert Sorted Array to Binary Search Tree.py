# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    root = TreeNode()
    stack: list = [(0, len(nums), root)]

    while stack:
        i, j, node = stack.pop()
        mid = (i + j) // 2
        node.val = nums[mid]
        
        if mid > i:
            node.left = TreeNode()
            stack.append((i, mid, node.left))
        if mid+1 < j:
            node.right = TreeNode()
            stack.append((mid+1, j, node.right))
            
    return root
