# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def dfs(original,cloned):
        if not original: return
        elif original == target: return cloned
        else: return (
            dfs(original.left,cloned.left) or 
            dfs(original.right,cloned.right)
        )
    
    return dfs(original,cloned)
