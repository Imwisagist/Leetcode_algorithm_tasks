# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q: return root

    l, r = lowestCommonAncestor(root.left, p, q), lowestCommonAncestor(root.right, p, q)

    if l and r: return root

    return l or r
