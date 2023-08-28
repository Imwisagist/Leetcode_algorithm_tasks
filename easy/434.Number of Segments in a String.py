# https://leetcode.com/problems/number-of-segments-in-a-string/

def countSegments(s: str) -> int:
    return len(s.split())


assert countSegments("Hello, my name is John") == 5
assert countSegments("Hello") == 1
