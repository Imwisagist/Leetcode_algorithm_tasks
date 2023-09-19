# https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/

from collections import Counter

def equalFrequency(word: str) -> bool:
    freq = sorted(Counter(word).values())
    freq[0] -= 1
    
    if len(set(filter(None, freq))) == 1:
        return True

    freq[0] += 1; freq[-1] -= 1

    return len(set(filter(None, freq))) == 1


assert equalFrequency("abcc") is True
assert equalFrequency("aazz") is False
