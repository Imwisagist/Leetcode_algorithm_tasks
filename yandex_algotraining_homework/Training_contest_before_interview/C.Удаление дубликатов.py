# https://contest.yandex.ru/contest/8458/

prev,unique = float("-inf"),[]

for _ in range(int(input())):
    num = int(input())
    
    if num > prev: unique.append(num)

    prev = num

print(*unique, sep='\n')
