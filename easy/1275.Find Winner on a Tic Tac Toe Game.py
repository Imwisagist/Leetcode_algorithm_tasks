# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/

from typing import List

def tictactoe(moves: List[List[int]]) -> str:
    win = (
        {(0,0),(0,1),(0,2)}, {(0,0),(1,0),(2,0)},
        {(1,0),(1,1),(1,2)}, {(0,1),(1,1),(2,1)},
        {(2,0),(2,1),(2,2)}, {(0,2),(1,2),(2,2)},
        {(0,0),(1,1),(2,2)}, {(0,2),(1,1),(2,0)},
    )
    length, moves = len(moves), map(tuple, moves)
    A, B, even = set(), set(), True

    for move in moves:
        if even: A.add(move); even = False
        else: B.add(move); even = True

    for win_case in win:
        if win_case <= A: return "A"
        if win_case <= B: return "B"
    
    return "Pending" if length < 9 else "Draw"


assert tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]) == "A"
assert tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]) == "B"
assert tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]) == "Draw"
assert tictactoe([[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]) == "A"
