from bisect import bisect_left
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    sub = [nums[0]]

    for num in nums[1:]:
        if num > sub[-1]: sub.append(num)
        else:
            i = bisect_left(sub, num)
            sub[i] = num

    return len(sub)


assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
assert lengthOfLIS([2, 5, 7, 5, 2, 3, 10, 9]) == 4
