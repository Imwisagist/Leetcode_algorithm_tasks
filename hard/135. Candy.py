# https://leetcode.com/problems/candy/description/
from typing import List


def candy(ratings: List[int]) -> int:
    n = len(ratings); candies = [1]*n

    for i in range(1, n):
        if ratings[i] > ratings[i-1]: candies[i] = candies[i-1] + 1

    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]: candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)


assert candy([1, 3, 2, 2, 1]) == 7
assert candy([1, 0, 2]) == 5
assert candy([1, 2, 2]) == 4
