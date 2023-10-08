# https://leetcode.com/problems/available-captures-for-rook/description/

from typing import List

def numRookCaptures(board: List[List[str]]) -> int:
    res,found = 0,False

    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell == "R": found = True; break

        if found: break

    col_after = (board[i][j] for i in range(i+1,len(board)))
    col_before,row = [board[i][j] for i in range(i)],board[i]

    for i in row[j+1:]:
        if i == "p": res += 1; break
        elif i == "B": break

    for i in reversed(row[:j]):
        if i == "p": res += 1; break
        elif i == "B": break

    for i in col_after:
        if i == "p": res += 1; break
        elif i == "B": break

    for i in reversed(col_before):
        if i == "p": res += 1; break
        elif i == "B": break

    return res 


assert numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 3
assert numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 0
assert numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 3
