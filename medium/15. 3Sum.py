# https://leetcode.com/problems/3sum/description/
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []; nums.sort()

    for i, num in enumerate(nums):
        if num > 0: break
        if i > 0 and num == nums[i - 1]: continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            three_sum = num + nums[l] + nums[r]

            if three_sum > 0: r -= 1
            elif three_sum < 0: l += 1
            else:
                res.append([num, nums[l], nums[r]]); l += 1; r -= 1

                while nums[l] == nums[l - 1] and l < r: l += 1

    return res


assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert threeSum([0, 1, 1]) == []
assert threeSum([0, 0, 0]) == [[0, 0, 0]]
