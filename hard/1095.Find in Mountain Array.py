"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""

class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass


def findInMountainArray(target: int, mountain_arr: MountainArray) -> int:
    def bin_search(lo,hi,mult):
        while lo < hi: 
            mid = lo + hi >> 1

            if mountain_arr.get(mid) == target: return mid 
            elif mountain_arr.get(mid)*mult < target*mult: lo = mid + 1
            else: hi = mid

        return -1 
    
    lo,hi = 0,mountain_arr.length()

    while lo < hi: 
        mid = lo + hi >> 1

        if mid and mountain_arr.get(mid-1) < mountain_arr.get(mid): lo = mid + 1
        else: hi = mid 
        
    if (x := bin_search(0,lo,1)) != -1: return x

    if (x := bin_search(lo,mountain_arr.length(),-1)) != -1: return x

    return -1 
