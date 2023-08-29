# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: Optional[TreeNode]) -> List[int]:
        mode, freq_max, last, freq = [root.val], 1, float('inf'), 0

        def in_order(node):
            nonlocal mode, freq_max, last, freq
            
            if node.left:
                in_order(node.left)

            if last == node.val:
                freq += 1
            else:
                if freq > freq_max:
                    freq_max, mode = freq, [last]
            
                elif freq == freq_max:
                    mode.append(last)
                    
                freq = 1
                last = node.val

            if node.right:
                in_order(node.right)

        in_order(root)

        if freq > freq_max:
            return [last]
        elif freq == freq_max:
                mode.append(last)
    
        if freq_max == 1:
            return mode[1:]

        return mode


tree1 = TreeNode(1)
tree1.right = TreeNode(2)
tree1.right.left = TreeNode(2)

assert findMode(tree1) == [2]
