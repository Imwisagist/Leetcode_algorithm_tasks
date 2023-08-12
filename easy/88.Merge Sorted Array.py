# https://leetcode.com/problems/merge-sorted-array/

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

    return nums1


assert merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [1, 2, 2, 3, 5, 6]
