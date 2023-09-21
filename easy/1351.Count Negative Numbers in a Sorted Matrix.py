# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

from typing import List

def countNegatives(grid: List[List[int]]) -> int:
    cnt, lenght = 0, len(grid[0])

    for nums in grid:
        l, r = 0, lenght - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < 0: r = m - 1
            else: l = m + 1

        cnt += lenght - l

    return cnt


assert countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]) == 8
assert countNegatives([[3,2],[1,0]]) == 0
