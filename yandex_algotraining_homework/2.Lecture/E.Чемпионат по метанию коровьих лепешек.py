# https://contest.yandex.ru/contest/27472/enter/

def solve(throws):
    winner_throw = throws[0]; winner_was_before = True
    vasya_best_throw = None; vasya_best_placement = 1

    for i in range(1, len(throws) - 1):
        throw = throws[i]

        if throw > winner_throw:
            winner_throw = throw; winner_was_before = True
            vasya_best_throw = None
        else:
            if winner_was_before:
                if throw % 10 == 5 and throws[i + 1] < throw:
                    if not vasya_best_throw or vasya_best_throw < throw:
                        vasya_best_throw = throw

    if not vasya_best_throw: return 0

    for throw in throws:
        if throw > vasya_best_throw: vasya_best_placement += 1

    return vasya_best_placement


n = int(input())
nums = list(map(int, input().split()))

print(solve(nums))
