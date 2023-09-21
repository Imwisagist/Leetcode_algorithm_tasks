# https://contest.yandex.ru/contest/27472/enter/

def solve(nums):
    m1p, m2p, m3p = sorted(nums[:3], reverse=True)
    m1n, m2n = m3p, m2p

    for num in nums[3:]:
        if num > m3p:
            if num > m2p:
                if num > m1p: m1p, m2p, m3p = num, m1p, m2p
                else: m2p, m3p = num, m2p
            else: m3p = num
        
        elif num < m2n:
            if num < m1n: m1n, m2n = num, m1n
            else: m2n = num

    return (m1p, m2p, m3p) if m1p*m2p*m3p >= m1n*m2n*m1p else (m1p, m2n, m1n)


nums = list(map(int, input().split()))

print(*solve(nums))
