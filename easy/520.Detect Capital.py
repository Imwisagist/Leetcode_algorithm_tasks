# https://leetcode.com/problems/detect-capital/

def detectCapitalUse(word: str) -> bool:
    if len(word) < 2:
        return True

    if word[0].islower():
        for i in word:
            if not i.islower(): return False

    elif word[0].isupper():
        if word[1].isupper():
            for i in word:
                if not i.isupper(): return False
        else:
            for i in word[1:]:
                if not i.islower(): return False
    
    return True


assert detectCapitalUse("USA") is True
assert detectCapitalUse("FlaG") is False
assert detectCapitalUse("Leetcode") is True
