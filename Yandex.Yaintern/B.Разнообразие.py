# https://contest.yandex.ru/contest/51022/enter/

from collections import defaultdict

n,m,q = map(int,input().split())
player_a,player_b = defaultdict(int),defaultdict(int)
diversity,result = 0,[]

for n in map(int,input().split()): player_a[n] += 1

for n in map(int,input().split()): player_b[n] += 1

for k,v in player_a.items(): diversity += abs(player_b.get(k,0)-v)

for k, v in player_b.items():
    if player_a.get(k,0) == 0: diversity += v

for q in range(q):
    type,player,card = input().split(); type, card = int(type), int(card)
    diff_before = abs(player_a.get(card,0) - player_b.get(card,0))

    if type == 1:
        if player == 'A': player_a[card] += 1
        else: player_b[card] += 1
    else:
        if player == 'A': 
            player_a[card] -= 1

            if player_a[card] == 0: del player_a[card]
        else:
            player_b[card] -= 1

            if player_b[card] == 0: del player_b[card]

    diff_after = abs(player_a.get(card,0)-player_b.get(card,0))
    diversity += diff_after - diff_before; result.append(diversity)

print(*result)
