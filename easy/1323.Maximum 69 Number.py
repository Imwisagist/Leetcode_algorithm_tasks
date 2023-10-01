# https://leetcode.com/problems/maximum-69-number/description/

def maximum69Number (num: int) -> int:
    return int(str(num).replace("6","9",1))


assert maximum69Number(9669) == 9969
assert maximum69Number(9996) == 9999
assert maximum69Number(9999) == 9999
