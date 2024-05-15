# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
import math
from typing import List


def maxDistToClosest(seats: List[int]) -> int:
    res, last = 0, -1

    for first, v in enumerate(seats):
        if v:
            res = max(res, first if last < 0 else (first - last) // 2)
            last = first

    return max(res, len(seats) - last - 1)

    # ones_arr = [i for i in range(len(seats)) if seats[i]]
    # dist_to_closest_per = 1
    #
    # if len(ones_arr) > 1:
    #     l, r = 0, 1
    # else:
    #     l = r = 0
    #
    # for i in range(len(seats)):
    #     if not seats[i]:
    #         dist_to_closest_per = max(dist_to_closest_per, min(abs(ones_arr[l] - i), abs(ones_arr[r] - i)))
    #     if i == ones_arr[r] and r < len(ones_arr) - 1:
    #         l += 1
    #         r += 1
    #
    # return dist_to_closest_per

    # res, prev, n = 0, -1, len(seats) - 1
    #
    # for i, v in enumerate(seats):
    #     if v:
    #         dist = i if prev == -1 else (i - prev) // 2
    #         res = max(res, dist)
    #         prev = i
    #
    # if not seats[n]: res = max(res, n - prev)
    #
    # return res


assert maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
assert maxDistToClosest([1, 0, 0, 0]) == 3
assert maxDistToClosest([0, 1]) == 1
