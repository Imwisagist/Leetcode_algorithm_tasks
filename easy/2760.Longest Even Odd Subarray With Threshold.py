# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/description/

from typing import List

def longestAlternatingSubarray(nums: List[int], threshold: int) -> int:
    cnt = res = 0; prev_even = False

    for n in nums:
        even = n % 2 == 0

        if n > threshold or even == prev_even:
            res = res if res > cnt else cnt; cnt = 0

        cnt += (n <= threshold) and (even or cnt > 0); prev_even = even

    return res if res > cnt else cnt


assert longestAlternatingSubarray([3,2,5,4],5) == 3
assert longestAlternatingSubarray([1,2],2) == 1
assert longestAlternatingSubarray([2,3,4,5],4) == 3
