# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val,self.left,self.right = val,left,right


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    q,res = deque([root]),[]

    while q:
        qlen,sum = len(q),0

        for _ in range(qlen):
            node = q.popleft(); sum += node.val

            if node.left: q.append(node.left)

            if node.right: q.append(node.right)

        res.append(sum/qlen)

    return res
