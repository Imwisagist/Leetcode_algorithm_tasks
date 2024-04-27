# https://leetcode.com/problems/reconstruct-itinerary/description/
from typing import List
from collections import defaultdict


def findItinerary(tickets: List[List[str]]) -> List[str]:
    d, n = defaultdict(list), len(tickets)
    stack, res = ["JFK"], [""] * (n + 1)

    for _from, _to in sorted(tickets, reverse=True): d[_from].append(_to)

    while stack:
        while d[key := stack[-1]]: stack.append(d[key].pop())
        res[n] = stack.pop(); n -= 1

    return res


assert findItinerary(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
assert findItinerary(
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
