# https://leetcode.com/problems/count-square-sum-triples/description/

import math


def countTriples(n: int) -> int:
	res = 0

	for i in range(1,n):
		for j in range(i+1,n):
			s = math.sqrt(i*i + j*j)
			
			if not s % 1 and s <= n: res += 2

	return res


assert countTriples(5) == 2
assert countTriples(10) == 4
