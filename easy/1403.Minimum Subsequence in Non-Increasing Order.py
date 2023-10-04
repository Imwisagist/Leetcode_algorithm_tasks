# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/

from typing import List

def minSubsequence(nums: List[int]) -> List[int]:
    nums.sort(reverse=True); s = nums.pop(0)
    res,n = [s],sum(nums)

    for i in nums:
        if n < s: break
        else: s += i; n -= i; res.append(i)

    return res


assert minSubsequence([4,3,10,9,8]) == [10,9]
assert minSubsequence([4,4,7,6,7]) == [7,7,6]
