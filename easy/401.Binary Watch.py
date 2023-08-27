# https://leetcode.com/problems/binary-watch/

from typing import List

def readBinaryWatch(turnedOn: int) -> List[str]:
    return [str(h)+':'+'0'*(m<10)+str(m) for h in range(12) for m in range(60) if (bin(m)+bin(h)).count('1') == turnedOn]


assert readBinaryWatch(1) == ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
assert readBinaryWatch(9) == []
