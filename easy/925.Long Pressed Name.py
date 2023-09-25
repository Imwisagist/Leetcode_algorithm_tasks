# https://leetcode.com/problems/long-pressed-name/description/

def isLongPressedName(name: str, typed: str) -> bool:
    l = r = 0; l2, r2 = len(name), len(typed)

    while l <= l2 and r < r2:
        if l < l2 and typed[r] == name[l]:
            l += 1; r += 1
        elif typed[r] == name[l-1] and l != 0:
            r += 1
        else: return False
        
    return l == l2 and r == r2


assert isLongPressedName("alex", "aleex") is True
assert isLongPressedName("saeed", "ssaaedd") is False
