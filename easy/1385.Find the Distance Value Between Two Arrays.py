# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

from typing import List

def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    cnt, lenght = len(arr1), len(arr2); arr2.sort()

    for num in arr1:
        l, r = 0, lenght - 1

        while l <= r:
            m = (l + r) // 2; target = arr2[m]

            if abs(num - target) <= d: cnt -= 1; break
            elif target > num: r = m - 1
            else: l = m + 1

    return cnt


assert findTheDistanceValue([4,5,8],[10,9,1,8],2) == 2
assert findTheDistanceValue([1,4,2,3],[-4,-3,6,10,20,30],3) == 2
assert findTheDistanceValue([2,1,100,3],[-5,-2,10,-3,7],6) == 1
