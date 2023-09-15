# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/

def digitCount(num: str) -> bool:
    for i, v in enumerate(num):
        if num.count(str(i)) != int(v): return False
    
    return True 


assert digitCount("1210") is True
assert digitCount("030") is False
