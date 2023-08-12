# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.

def isBadVersion(version: int) -> bool:
    pass

def firstBadVersion(n: int) -> int:
    left, right = 1, n

    while left < right:
        middle = (left + right) // 2
        if isBadVersion(middle):
            right = middle
        else:
            left = middle + 1

    return left
