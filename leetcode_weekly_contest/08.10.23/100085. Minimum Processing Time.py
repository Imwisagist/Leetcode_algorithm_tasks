from typing import List

def minProcessingTime(processorTime: List[int], tasks: List[int]) -> int:
    m = 0; tasks.sort(); processorTime.sort(reverse=True)

    for i,p in enumerate(processorTime):
        for t in tasks[i*4:i*4+4]: m = max(m,t+p)

    return m


assert minProcessingTime([8,10],[2,2,3,1,8,7,4,5]) == 16
assert minProcessingTime([10,20],[2,3,1,2,5,8,4,3]) == 23
