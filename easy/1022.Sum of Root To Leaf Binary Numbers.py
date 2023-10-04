# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val,self.left,self.right = val,left,right


def sumRootToLeaf(root: Optional[TreeNode]) -> int:
    stack,res = [(root,str(root.val))],0; sa = stack.append
    
    while stack:
        node,bin_val = stack.pop()

        if not node.left and not node.right: res += int(bin_val,2)
        else:
            if node.left: sa((node.left,bin_val+str(node.left.val)))
            
            if node.right: sa((node.right,bin_val+str(node.right.val)))

    return res


tree = TreeNode(1)
tree.left = TreeNode(0)
tree.right = TreeNode(1)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(1)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(1)

assert sumRootToLeaf(tree) == 22

tree2 = TreeNode(0)

assert sumRootToLeaf(tree2) == 0
