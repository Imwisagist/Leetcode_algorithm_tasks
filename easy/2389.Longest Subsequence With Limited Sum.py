# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

from typing import List

def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
    res, length, s, prefix_sum = [], len(nums) - 1, 0, []

    for n in sorted(nums): s += n; prefix_sum.append(s)

    for query in queries:
        l, r = 0, length

        while l <= r:
            m = (l + r + 1) // 2

            if prefix_sum[m] <= query: l = m + 1
            else: r = m - 1

        res.append(l)

    return res


assert answerQueries([4,5,2,1],[3,10,21]) == [2,3,4]
assert answerQueries([2,3,4,5],[1]) == [0]