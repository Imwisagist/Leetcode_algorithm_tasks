# https://leetcode.com/problems/find-center-of-star-graph/description/

from typing import List

def findCenter(edges: List[List[int]]) -> int:
    n1,n2 = edges[0]; n3,n4 = edges[1]

    return (
        n1 if n1 == n2 or n1 == n3 or n1 == n4 else 
        n2 if n2 == n3 or n2 == n4 else 
        n3
    )

assert findCenter([[1,2],[2,3],[4,2]]) == 2
assert findCenter([[1,2],[5,1],[1,3],[1,4]]) == 1
