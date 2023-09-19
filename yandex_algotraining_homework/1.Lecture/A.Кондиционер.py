# https://contest.yandex.ru/contest/27393/enter/

def decision(room_tmp, wish_tmp, mode):
    actions = {
        "freeze": lambda x,y: min(x, y),
        "heat": lambda x,y: max(x, y),
        "fan": lambda x,y: x, "auto": lambda x,y: y,
    }
    return actions[mode](room_tmp, wish_tmp)

room_tmp, wish_tmp = map(int, input().split())
mode = input()

print(decision(room_tmp, wish_tmp, mode))
