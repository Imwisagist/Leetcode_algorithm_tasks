# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/

from typing import List

def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    seats.sort(); students.sort()

    return sum(abs(se-st) for se,st in zip(seats,students))


assert minMovesToSeat([3,1,5],[2,7,4]) == 4
assert minMovesToSeat([4,1,5,9],[1,3,2,6]) == 7
assert minMovesToSeat([2,2,6,6],[1,3,2,6]) == 4
