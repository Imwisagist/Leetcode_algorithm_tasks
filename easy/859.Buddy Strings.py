# https://leetcode.com/problems/buddy-strings/


def buddyStrings(s: str, goal: str) -> bool:
    n, i = len(s), 0
    j: int = n - 1

    if len(goal) != n:
        return False

    if s == goal:
        temp = set(s)
        return len(temp) < len(goal)

    while i < j and s[i] == goal[i]:
        i += 1

    while j >= 0 and s[j] == goal[j]:
        j -= 1

    if i < j:
        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        s = ''.join(s_list)

    return s == goal


assert buddyStrings("ab", "ba") is True
assert buddyStrings("ab", "ab") is False
assert buddyStrings("aa", "aa") is True
