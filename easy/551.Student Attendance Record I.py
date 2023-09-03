# https://leetcode.com/problems/student-attendance-record-i/

def checkRecord(s: str) -> bool:
    count_l, absent = 0, False

    for i in s:
        if i == "A":
            if absent:
                return False
            absent = True
            count_l = 0

        elif i == "L":
            if count_l == 2:
                return False
            count_l += 1

        else:
            count_l = 0
    
    return True


assert checkRecord("PPALLP") is True
assert checkRecord("PPALLL") is False
