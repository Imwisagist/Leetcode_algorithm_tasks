# https://leetcode.com/problems/maximum-number-of-balloons/description/

def maxNumberOfBalloons(text: str) -> int:
    d: dict = {}
    d_get = d.get

    for i in text: d[i] = d_get(i,0) + 1

    return min(
        d_get("b",0), d_get("a",0), d_get("n",0),
        d_get("l",0)//2, d_get("o",0)//2
    )


assert maxNumberOfBalloons("nlaebolko") == 1
assert maxNumberOfBalloons("loonbalxballpoon") == 2
assert maxNumberOfBalloons("leetcode") == 0
