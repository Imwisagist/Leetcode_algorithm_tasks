# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/?envType=daily-question&envId=2023-10-02

def winnerOfGame(colors: str) -> bool:
    cnt_a = cnt_b = cur_a = cur_b = 0

    for c in colors:
        if c == "A":
            cur_a += 1; cur_b = 0

            if cur_a > 2: cnt_a += 1

        else:
            cur_b += 1; cur_a = 0

            if cur_b > 2: cnt_b += 1

    return cnt_a > cnt_b


assert winnerOfGame("AAABABB") is True
assert winnerOfGame("AA") is False
assert winnerOfGame("ABBBBBBBAAA") is False
