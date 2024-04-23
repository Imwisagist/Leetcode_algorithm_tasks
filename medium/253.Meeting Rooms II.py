# https://leetcode.com/problems/meeting-rooms-ii/description/
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    scan_line, cnt, res = [], 0, 0

    for start, end in intervals:
        scan_line.append((start, 1))
        scan_line.append((end, 0))

    scan_line.sort()

    for time, type in scan_line:
        if type:
            cnt += 1
        else:
            cnt -= 1

        res = max(res, cnt)

    return res

# ans = [0] Решение через кучу
#
#         for a, b in sorted(intervals):
#             if a < ans[0]:
#                 heapq.heappush(ans, b)
#             else:
#                 heapq.heapreplace(ans, b)
#
#         return len(ans)


assert minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
assert minMeetingRooms([[7, 10], [2, 4]]) == 1