# https://leetcode.com/problems/most-common-word/

from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    freq, max_freq, max_word = {}, 0, ""
    banned = set(banned)
    
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
    
    words = paragraph.lower().split()
    
    for word in words:
        if word not in banned:
            freq[word] = freq.get(word, 0) + 1

    for word, count in freq.items():
        if count > max_freq:
            max_freq = count
            max_word = word
    
    return max_word


assert mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball"
assert mostCommonWord("a.", []) == "a"
