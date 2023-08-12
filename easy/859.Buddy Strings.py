# https://leetcode.com/problems/buddy-strings/

def buddyStrings(s: str, goal: str) -> bool:
    r, l = len(s) - 1, 0

    if len(goal) != r + 1:
        return False

    if s == goal:
        temp = set(s)
        return len(temp) < len(goal)

    while l < r and s[l] == goal[l]:
        l += 1

    while r >= 0 and s[r] == goal[r]:
        r -= 1

    if l < r:
        arr: list = list(s)
        arr[l], arr[r] = arr[r], arr[l]
        s: str = ''.join(arr)

    return s == goal


assert buddyStrings("ab", "ba") is True
assert buddyStrings("ab", "ab") is False
assert buddyStrings("aa", "aa") is True
