# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/

from heapq import heappush, heappop

def largestInteger(num: int) -> int:
    idxs,heap_odd,heap_even,res = [],[],[],0

    while num:
        digit = num % 10; num //= 10

        if digit % 2 == 0: idxs.append(0); heappush(heap_even,digit)
        else: idxs.append(1); heappush(heap_odd,digit)

    for i,v in enumerate(idxs):
        if v: res += heappop(heap_odd) * (10**i)
        else: res += heappop(heap_even) * (10**i)

    return res


assert largestInteger(1234) == 3412
assert largestInteger(65875) == 87655
