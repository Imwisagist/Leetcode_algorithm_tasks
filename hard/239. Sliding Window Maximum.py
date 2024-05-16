# https://leetcode.com/problems/sliding-window-maximum/description/
from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    window = deque(maxlen=k)
    left = 0

    for right, val in enumerate(nums):
        while window and window[-1] < val: window.pop()
        window.append(val)

        if right + 1 >= k:
            res.append(window[0])

            if window[0] == nums[left]: window.popleft()
            left += 1

    return res


assert maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert maxSlidingWindow([1], 1) == [1]
