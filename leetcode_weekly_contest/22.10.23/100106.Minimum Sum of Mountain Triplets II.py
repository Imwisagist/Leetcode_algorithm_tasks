from typing import List


def minimumSum(nums: List[int]) -> int:
    minSum = float('inf'); n = len(nums)

    for i in range(n-2):
        if nums[i] >= nums[i+1]: continue

        for j in range(i+1,n-1):
            if nums[j] <= nums[i]: continue

            for k in range(j+1,n):
                if nums[k] >= nums[j]: continue

                sum = nums[i] + nums[j] + nums[k]

                if sum < minSum: minSum = sum

    if minSum == float('inf'): return -1
    
    return minSum


assert minimumSum([50,50,50]) == -1
assert minimumSum([8,6,1,5,3]) == 9
assert minimumSum([5,4,8,7,10,2]) == 13
assert minimumSum([6,5,4,3,4,5]) == -1
#TL