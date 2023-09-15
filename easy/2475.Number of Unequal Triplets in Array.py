# https://leetcode.com/problems/number-of-unequal-triplets-in-array/description/

from typing import List

def unequalTriplets(nums: List[int]) -> int:
    prev, next, counter, d = 0, len(nums), 0, {}
    d_get = d.get

    for i in nums: d[i] = d_get(i,0) + 1

    for frequency in d.values():
        next -= frequency
        counter += prev * frequency * next
        prev += frequency

    return counter


assert unequalTriplets([4,4,2,4,3]) == 3
assert unequalTriplets([1,1,1,1,1]) == 0

# or the following bruteforce
# counter: int = 0

# for i1,n1 in enumerate(nums[:-2]):
#     for i2,n2 in enumerate(nums[i1+1:-1],i1+1):
#         if n1 != n2:
#             for n3 in nums[i2+1:]:
#                 if n3!=n1 and n3!=n2: counter += 1

# return counter
# or this unreadable one line program - return sum(1 for i1,n1 in enumerate(nums[:-2]) for i2,n2 in enumerate(nums[i1+1:-1],i1+1) if n1 != n2 for n3 in nums[i2+1:] if n3!=n1 and n3!=n2)
