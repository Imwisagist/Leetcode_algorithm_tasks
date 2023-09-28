# https://contest.yandex.ru/contest/51022/enter/

stack,stack_a,stack_b = [0],[[0, 0]],[[0, 0]]
n = int(input()); result = [0] * n
lang = ['0'] + input().split(); lang_a = lang_b = idx = 0
p = list(map(int,input().split()))

for i in range(1,2*(n+1)-1):
    if stack[idx] == p[i]:
        if lang[p[i]] == 'A':
            cnt = idx - stack_a[lang_a-1][1] - 1
            lang_a -= 1; stack_a.pop()

        else:
            cnt = idx - stack_b[lang_b-1][1] - 1
            lang_b -= 1; stack_b.pop()

        result[p[i]-1] = cnt; stack.pop(); idx -= 1

    else:
        stack.append(p[i]); idx += 1

        if lang[p[i]] == 'A':
            lang_a += 1; stack_a.append([p[i],idx])
        else:
            lang_b += 1; stack_b.append([p[i],idx])

print(*result)
