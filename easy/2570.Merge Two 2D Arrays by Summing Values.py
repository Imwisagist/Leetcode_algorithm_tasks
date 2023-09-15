# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

from typing import List

def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    result, l, r, n1l, n2l = [], 0, 0, len(nums1), len(nums2)

    while l < n1l or r < n2l:
        if l == n1l: result.append(nums2[r]); r += 1
        elif r == n2l: result.append(nums1[l]); l += 1
        else:
            if nums1[l][0] > nums2[r][0]:
                result.append(nums2[r]); r += 1

            elif nums1[l][0] < nums2[r][0]:
                result.append(nums1[l]); l += 1

            else:
                result.append([nums1[l][0], nums1[l][1]+nums2[r][1]])
                l += 1; r += 1

    return result


assert mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]) == [[1,6],[2,3],[3,2],[4,6]]
assert mergeArrays([[2,4],[3,6],[5,5]],[[1,3],[4,3]]) == [[1,3],[2,4],[3,6],[4,3],[5,5]]
