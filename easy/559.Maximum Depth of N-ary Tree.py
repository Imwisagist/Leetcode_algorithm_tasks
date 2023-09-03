# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(root: Node) -> int:
    if not root: return 0
        
    deq = deque([(root,1)])
    
    while deq:
        node, depth = deq.popleft()
        
        if node.children:
            for i in node.children:
                deq.append((i,depth+1))
    
    return depth


tree1 = Node(1)
tree1.children = [Node(3), Node(2), Node(4)]
tree1.children[0].children = [Node(5), Node(6)]

assert maxDepth(tree1) == 3

tree2 = Node(1)
tree2.children = [Node(2), Node(3), Node(4), Node(5)]
tree2.children[1].children = [Node(6), Node(7)]
tree2.children[1].children[1].children = [Node(11)]
tree2.children[1].children[1].children[0].children = [Node(14)]
tree2.children[2].children = [Node(8)]
tree2.children[2].children[0].children = [Node(12)]
tree2.children[3].children = [Node(9), Node(10)]
tree2.children[3].children[0].children = [Node(13)]

assert maxDepth(tree2) == 5
