# https://leetcode.com/problems/excel-sheet-column-number/

def titleToNumber(columnTitle: str) -> int:
    result, position = 0, len(columnTitle) - 1

    for letter in columnTitle:
        result += (ord(letter) - 64) * 26 ** position
        position -= 1
        
    return result


assert titleToNumber("A") == 1
assert titleToNumber("AB") == 28
assert titleToNumber("ZY") == 701
