# https://leetcode.com/problems/next-greater-element-i/

from typing import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater, stack = {}, []
    
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    return [next_greater[num] if num in next_greater else -1 for num in nums1]


assert nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
assert nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]
