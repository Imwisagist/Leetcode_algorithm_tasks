# https://leetcode.com/problems/path-sum/
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root: return False
    
    queue = deque([(root, root.val)])

    while queue:
        node, val = queue.popleft()
        if not node.left and not node.right:
            if val == targetSum: return True
            else: continue
        if node.left:
            queue.append((node.left, val + node.left.val))   
        if node.right:
            queue.append((node.right, val + node.right.val))   
    
    return False


tree1 = TreeNode(5)
tree1.left = TreeNode(4)
tree1.left.left = TreeNode(11)
tree1.left.left.left = TreeNode(7)
tree1.left.left.right = TreeNode(2)
tree1.right = TreeNode(8)
tree1.right.left = TreeNode(13)
tree1.right.right = TreeNode(4)
tree1.right.right.right = TreeNode(1)

assert hasPathSum(tree1, 22) is True

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

assert hasPathSum(tree2, 5) is False
