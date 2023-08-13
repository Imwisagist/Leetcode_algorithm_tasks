# https://leetcode.com/problems/ransom-note/

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for i in ransomNote:
        if i not in magazine:
            return False
        else:
            magazine = magazine.replace(i, '', 1)

    return True


assert canConstruct("a", "b") is False
assert canConstruct("aa", "ab") is False
assert canConstruct("aa", "aab") is True
