# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/

import heapq
from typing import List

def maxSubsequence(nums: List[int], k: int) -> List[int]:
    d, res = {}, []; d_get = d.get

    for n in heapq.nlargest(k,nums):
        d[n] = d_get(n,0) + 1

    for n in nums:
        if d_get(n,0):
            d[n] -= 1; res.append(n)

    return res


assert maxSubsequence([2,1,3,3],2) == [3,3]
assert maxSubsequence([-1,-2,3,4],3) == [-1,3,4]
assert maxSubsequence([3,4,3,3],2) == [3,4]
