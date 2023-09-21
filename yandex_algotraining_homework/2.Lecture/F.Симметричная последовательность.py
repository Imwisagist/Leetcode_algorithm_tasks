# https://contest.yandex.ru/contest/27472/enter/

def is_symmetric(nums):
    for i in range(len(nums) // 2):
        if nums[i] != nums[-1 - i]: return False

    return True

def solve(nums):
    for i in range(len(nums)):
        if is_symmetric(nums[i:]): return nums[:i][::-1]


n = int(input())
nums = list(map(int, input().split()))

result = solve(nums)

print(len(result))

if len(result): print(*result)
