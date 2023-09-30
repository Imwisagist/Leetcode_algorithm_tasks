# https://leetcode.com/problems/increasing-order-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def increasingBST(node: TreeNode) -> TreeNode:
    dummy = tail = TreeNode()

    while node:
        if node.left:
            predecessor = node.left
            
            while predecessor.right: predecessor = predecessor.right
            
            predecessor.right = node; left, node.left = node.left, None; node = left

        else: tail.right = tail = node; node = node.right
    
    return dummy.right


tree1 = TreeNode(5)
tree1.left = TreeNode(3)
tree1.right = TreeNode(6)
tree1.left.left = TreeNode(2)
tree1.left.right = TreeNode(4)
tree1.left.left.left = TreeNode(1)
tree1.right.right = TreeNode(8)
tree1.right.right.left = TreeNode(7)
tree1.right.right.right = TreeNode(9)

increasingBST(tree1)