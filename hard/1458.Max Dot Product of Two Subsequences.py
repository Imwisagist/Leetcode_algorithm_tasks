# https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/?envType=daily-question&envId=2023-10-08

from typing import List

def maxDotProduct(nums1: List[int], nums2: List[int]) -> int:
    m,n = len(nums1),len(nums2)
    cur = [float('-inf')] * (n+1); prev = cur.copy()
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            curp = nums1[i-1] * nums2[j-1]
            cur[j] = max(curp,prev[j],cur[j-1],curp+max(0,prev[j-1]))
        
        cur,prev = prev,cur
    
    return prev[n]


assert maxDotProduct([2,1,-2,5],[3,0,-6]) == 18
assert maxDotProduct([3,-2],[2,-6,7]) == 21
assert maxDotProduct([-1,-1],[1,1]) == -1
