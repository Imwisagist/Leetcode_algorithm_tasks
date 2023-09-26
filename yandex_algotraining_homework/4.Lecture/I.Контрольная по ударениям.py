# https://contest.yandex.ru/contest/27665/enter/

def solve(d, s):
    c = 0

    for word in s:
        if word not in d:
            capital = False

            for chr in word:
                if chr.isupper():
                    if capital: c += 1; break
                    
                    capital = True
            else:
                if not capital: c += 1

    return c


d = {input() for _ in range(int(input()))}
s = input().split()

print(solve(d, s))
