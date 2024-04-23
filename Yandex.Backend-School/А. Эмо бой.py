# https://contest.yandex.ru/contest/60242/problems/A/

def check_nickname(s: str) -> bool:
    if len(s) < 8: return False

    digit = lower = upper = False

    for chr in s:
        if not digit and chr.isdigit(): digit = True
        elif not lower and chr.islower(): lower = True
        elif not upper and chr.isupper(): upper = True

    return digit and lower and upper


print("YES" if check_nickname(input()) else "NO")
