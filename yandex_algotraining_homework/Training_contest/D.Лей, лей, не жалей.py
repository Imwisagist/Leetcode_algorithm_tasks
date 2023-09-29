# https://contest.yandex.ru/contest/50668/enter

# from collections import defaultdict

# def solve(orders):
#     res = []

#     for _ in range(int(input())):
#         start,end,type = map(int,input().split()); cnt = 0

#         if type == 1:
#             for interval,price in orders.items():
#                 if interval[0] >= start and interval[0] <= end:
#                     cnt += price
#         else:
#             for interval,price in orders.items():
#                 if interval[1] >= start and interval[1] <= end:
#                     cnt += interval[1] - interval[0]
        
#         res.append(cnt)
    
#     return res


# orders = defaultdict(int)

# for i in range(int(input())):
#     start,end,price = map(int,input().split())
#     orders[start,end] = price

# print(*solve(orders))
##############################################################
quests = []; costTaskStartedAt = {}; lenTaskEndedAt = {}

for i in range(int(input())):
    start, end, price = map(int, input().split())
    costTaskStartedAt[start] = costTaskStartedAt.get(start, 0) + price
    lenTaskEndedAt[end] = lenTaskEndedAt.get(end, 0) + end - start

numQuest = int(input())
for i in range(numQuest):
    s, e, t = map(int, input().split()); quests.append((s, e, t))
    costTaskStartedAt.setdefault(s-1, 0); costTaskStartedAt.setdefault(e, 0)
    lenTaskEndedAt.setdefault(s-1, 0); lenTaskEndedAt.setdefault(e, 0)

def makeCumulativeSum(map):
    currentSum = 0

    for key in sorted(map.keys()):
        currentSum += map[key]; map[key] = currentSum

makeCumulativeSum(costTaskStartedAt); makeCumulativeSum(lenTaskEndedAt)

for quest in quests:
    if quest[2] == 1: print(costTaskStartedAt[quest[1]] - costTaskStartedAt[quest[0]-1])
    else: print(lenTaskEndedAt[quest[1]] - lenTaskEndedAt[quest[0]-1])
    