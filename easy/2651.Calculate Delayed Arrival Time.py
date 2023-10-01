# https://leetcode.com/problems/calculate-delayed-arrival-time/description/

def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
    return (arrivalTime + delayedTime) % 24


assert findDelayedArrivalTime(15,5) == 20
assert findDelayedArrivalTime(13,11) == 0
