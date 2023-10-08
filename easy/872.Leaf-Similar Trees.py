# https://leetcode.com/problems/leaf-similar-trees/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val,self.left,self.right = val,left,right


def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs(root):  
        if not root: return []                 
                                                    
        if not root.left and not root.right: return [root.val]                  
                                                
        return dfs(root.left) + dfs(root.right)
                                        
    return dfs(root1) == dfs(root2)
