# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j, output = 0, 0, []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                output.append(nums1[i])
                i += 1
                j += 1

        return output


assert intersect([1,2,2,1], [2,2]) == [2,2]
assert intersect([4,9,5], [9,4,9,8,4]) == [4,9]
