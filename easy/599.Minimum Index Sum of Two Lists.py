# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

from typing import List

def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    def result(l1, l2) -> List[str]:
        hashmap, result, min_idx = {}, [], len(list1) + len(list2) - 2

        for idx, val in enumerate(l1):
            hashmap[val] = idx

        for idx, val in enumerate(l2):
            if val in hashmap and hashmap[val] + idx <= min_idx:
                if hashmap[val] + idx < min_idx:
                    result.clear()
                    min_idx = hashmap[val] + idx
                result.append(val)

        return result

    return result(list1, list2) if len(list1) < len(list2) else result(list2, list1)


assert findRestaurant(
    ["Shogun","Tapioca Express","Burger King","KFC"],
    ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
) == ["Shogun"]

assert findRestaurant(
    ["Shogun","Tapioca Express","Burger King","KFC"],
    ["KFC","Shogun","Burger King"]
) == ["Shogun"]

assert findRestaurant(
    ["happy","sad","good"], ["sad","happy","good"]
) == ["happy","sad"]
