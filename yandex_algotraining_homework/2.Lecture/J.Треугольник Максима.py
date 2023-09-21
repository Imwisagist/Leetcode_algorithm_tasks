# https://contest.yandex.ru/contest/27472/enter/

def solve(prev, arr):
    left, right = 30.0, 4000.0
    
    for freq, word in arr:
        freq = float(freq)

        if abs(freq - prev) < 10**(-6): continue

        if word == "closer":
            if freq > prev: left = max(left,(freq + prev) / 2)
            else: right = min(right,(freq + prev) / 2)
        else:
            if freq < prev: left = max(left,(freq + prev) / 2)
            else: right = min(right,(freq + prev) / 2)
        
        prev = freq

    return left, right


n, start = int(input()), float(input())
arr = [input().split() for _ in range(n-1)]

print(*solve(start, arr))
