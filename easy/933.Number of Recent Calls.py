# https://leetcode.com/problems/number-of-recent-calls/description/
from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()
        
    def ping(self, t: int) -> int:
        queue, start = self.queue, t - 3000; queue.append(t)

        while queue and queue[0] < start: queue.popleft()

        return len(queue)
