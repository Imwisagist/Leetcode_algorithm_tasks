# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

from typing import List

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    result = []

    for idx, arr in enumerate(mat):
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m]: l = m + 1
            else: r = m - 1
        
        result.append((idx,l))

    return [x for x, _ in sorted(result,key=lambda x: x[1])[:k]]
            

assert kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3) == [2,0,3]
assert kWeakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],2) == [0,2]
assert kWeakestRows([[1,1,1,1,1],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,0],[1,1,1,1,1]],3) == [1,2,3]
