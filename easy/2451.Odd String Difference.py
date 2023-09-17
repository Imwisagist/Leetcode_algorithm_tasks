# https://leetcode.com/problems/odd-string-difference/description/
import string
from typing import List

def oddString(words: List[str]) -> str:
    s = string.ascii_lowercase.index

    def generate_list(w: str) -> list:
        return [s(w[j]) - s(w[j-1]) for j in range(1,length)]

    w1, w2 = words[-1], words[-2]; length = len(w1)
    diff1, diff2 = generate_list(w1), generate_list(w2)
    
    if diff1 != diff2:
        w3 = words[-3]; diff3 = generate_list(w3)

        if diff1 == diff3: return w2
        elif diff1 == diff2: return w3
        else: return w1

    for w in words:
        arr = generate_list(w)

        if diff1 != arr: return w
        

assert oddString(["adc","wzy","abc"]) == "abc"
assert oddString(["aaa","bob","ccc","ddd"]) == "bob"
