# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/

def areNumbersAscending(s: str) -> bool:
    nums = [int(w) for w in s.split() if w.isdigit()]

    return all(nums[i-1] < nums[i] for i in range(1,len(nums)))


assert areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles") is True 
assert areNumbersAscending("hello world 5 x 5") is False
assert areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s") is False
