# https://leetcode.com/problems/most-frequent-even-element/description/

from typing import List

def mostFrequentEven(nums: List[int]) -> int:
    d, max, res = {}, 0, -1; d_get = d.get

    for n in nums: 
        if n % 2 == 0: d[n] = d_get(n,0) + 1
    
    for num, count in d.items():
        if count >= max:
            if count > max: max = count; res = num
            else: res = min(num, res)

    return res


assert mostFrequentEven([0,1,2,2,4,4,1]) == 2
assert mostFrequentEven([4,4,4,9,2,4]) == 4
assert mostFrequentEven([29,47,21,41,13,37,25,7]) == -1
