# https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

def squareIsWhite(c: str) -> bool:
    return ord(c[0]) % 2 != int(c[1]) % 2


assert squareIsWhite("h3") is True
assert squareIsWhite("c7") is False
assert squareIsWhite("a1") is False
