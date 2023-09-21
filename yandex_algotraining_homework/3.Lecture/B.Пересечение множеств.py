# https://contest.yandex.ru/contest/27663/enter/

def solve(nums): 
    return sorted(set(nums[0])&set(nums[1]))


nums = [map(int,input().split()) for _ in range(2)]

print(*solve(nums))
