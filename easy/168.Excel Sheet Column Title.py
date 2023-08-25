# https://leetcode.com/problems/excel-sheet-column-title/

def convertToTitle(columnNumber: int) -> str:
    output: str = ""

    while columnNumber > 0:
        output = chr(65 + (columnNumber - 1) % 26) + output
        columnNumber = (columnNumber - 1) // 26

    return output


assert convertToTitle(1) == "A"
assert convertToTitle(28) == "AB"
assert convertToTitle(701) == "ZY"
