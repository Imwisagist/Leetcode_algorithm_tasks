# https://leetcode.com/problems/concatenation-of-array/description/

from typing import List

def getConcatenation(nums: List[int]) -> List[int]:
    return nums + nums


assert getConcatenation([1,2,1]) == [1,2,1,1,2,1]
assert getConcatenation([1,3,2,1]) == [1,3,2,1,1,3,2,1]
