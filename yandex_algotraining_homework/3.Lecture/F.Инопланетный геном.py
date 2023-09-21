# https://contest.yandex.ru/contest/27663/enter/

def solve(s1, s2): 
    s_gen = set()

    for i in range(1, len(s2)): s_gen.add(s2[i-1]+s2[i])

    return sum(1 for i in range(1, len(s1)) if s1[i-1]+s1[i] in s_gen)


first_gen, second_gen = input(), input()

print(solve(first_gen, second_gen))
