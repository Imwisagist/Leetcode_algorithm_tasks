# https://leetcode.com/problems/find-the-distinct-difference-array/description/

from typing import List

def distinctDifferenceArray(nums: List[int]) -> List[int]:

    def calculate(numbers: list) -> list:
        count, arr, seen = 0, [], set()

        for i in numbers:
            if i not in seen:
                seen.add(i)
                count += 1

            arr += [count]

        return arr

    prefix = calculate(nums)
    suffix = calculate(nums[::-1])[::-1]

    return [prefix[i] - suffix[i+1] for i in range(len(nums)-1)] + [prefix[-1]]


assert distinctDifferenceArray([1,2,3,4,5]) == [-3,-1,1,3,5]
assert distinctDifferenceArray([3,2,3,4,2]) == [-2,-1,0,2,3]
