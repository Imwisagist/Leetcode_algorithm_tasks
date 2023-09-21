# https://contest.yandex.ru/contest/27472/enter/

def solve(nums):
    m1p = max(nums[0], nums[1])
    m2p = min(nums[0], nums[1])
    m1n, m2n = m2p, m1p

    for num in nums[2:]:
        if num > m2p:
            if num > m1p: m1p, m2p = num, m1p
            else: m2p = num
        
        elif num < m2n:
            if num < m1n: m1n, m2n = num, m1n
            else: m2n = num

    return (m2p, m1p) if m1p * m2p >= m1n * m2n else (m1n, m2n)


nums = list(map(int, input().split()))

print(*solve(nums))
