# https://contest.yandex.ru/contest/50668/enter

def solve(logs):
    logs.sort(key=lambda x: (int(x[3]), x[0], x[1], x[2]))

    prev_id, cnt, res = logs[0][3], 0, []

    for day, hour, minute, id, status in logs:
        if status == 'B': continue

        if id != prev_id: res.append(cnt); cnt = 0; prev_id = id

        if status == 'A':
            cnt -= int(day) * 1440 + int(hour) * 60 + int(minute)
        else:
            cnt += int(day) * 1440 + int(hour) * 60 + int(minute)
    
    res.append(cnt)

    return res


logs = [input().split() for _ in range(int(input()))]

print(*solve(logs))
