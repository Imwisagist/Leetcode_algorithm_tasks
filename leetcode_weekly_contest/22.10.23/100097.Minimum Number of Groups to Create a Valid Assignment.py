from typing import List


def minGroupsForValidAssignment(nums: List[int]) -> int:
    freq = {}

    for num in nums: freq[num] = freq.get(num, 0) + 1
    
    max_freq = max(freq.values()); min_groups = 0

    for val in freq.values():
        if val != max_freq: min_groups += 1

    return min_groups

assert minGroupsForValidAssignment([3,2,3,2,3]) == 2
assert minGroupsForValidAssignment([10,10,10,3,1,1]) == 4
#WA