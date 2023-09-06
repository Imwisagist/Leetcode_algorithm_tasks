# https://leetcode.com/problems/shortest-completing-word/

from collections import Counter
from typing import List

def shortestCompletingWord(licensePlate: str, words: List[str]) -> str:
    license: str = ""
    words.sort(key=len)

    for i in licensePlate:
        if i.isalpha():
            license += i.lower()
        
    for word in words:
        for i,v in enumerate(license):
            if word.count(v) < license.count(v):
                break
            if i == len(license)-1:
                return word


assert shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]) == "steps"
assert shortestCompletingWord("1s3 456", ["looks","pest","stew","show"])
