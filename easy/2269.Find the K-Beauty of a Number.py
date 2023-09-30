# https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/

def divisorSubstrings(num: int,k: int) -> int:
    cnt,s = 0,str(num)

    for i in range(len(s)+1-k):
        div = int(s[i:i+k])

        if div:
            if num % div == 0: cnt += 1

    return cnt


assert divisorSubstrings(240,2) == 2
assert divisorSubstrings(430043,2) == 2
