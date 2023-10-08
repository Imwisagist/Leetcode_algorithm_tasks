# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/

def minLength(s: str) -> int:
    prev = len(s)+1

    while len(s) < prev:
        s,prev = s.replace('AB','').replace('CD',''),len(s)
    
    return prev


assert minLength("CCCCDDDD") == 0
assert minLength("ABFCACDB") == 2
assert minLength("ACBBD") == 5
