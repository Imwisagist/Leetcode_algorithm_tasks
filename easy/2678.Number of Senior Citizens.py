# https://leetcode.com/problems/number-of-senior-citizens/

from typing import List

def countSeniors(details: List[str]) -> int:
    return sum(1 for p in details if int(p[11:13]) > 60)


assert countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]) == 2
assert countSeniors(["1313579440F2036","2921522980M5644"]) == 0
