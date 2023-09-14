# https://leetcode.com/problems/destination-city/description/

from typing import List

def destCity(paths: List[List[str]]) -> str:
    d: dict = {from_: to_ for from_, to_ in paths}
    city: str = paths[0][0]

    while True:
        if city in d:
            city = d[city]
        else:
            break

    return city


assert destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]) == "Sao Paulo"
assert destCity([["B","C"],["D","B"],["C","A"]]) == "A"
assert destCity([["A","Z"]]) == "Z"
assert destCity([["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]]) == "OAxMijOZgW"
