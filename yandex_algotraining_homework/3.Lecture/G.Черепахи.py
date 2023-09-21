# https://contest.yandex.ru/contest/27663/enter/

def solve(statements): 
    prev_stat = set()

    for stat in statements:
        no_neg_stat= stat[0] >= 0 and stat[1] >= 0
        corr_num_of_turt = stat[0] + stat[1] + 1 == len(statements)
        
        if no_neg_stat and corr_num_of_turt and stat not in prev_stat:
            prev_stat.add(stat)

    return len(prev_stat)


turtle_statements = [tuple(map(int, input().split())) for _ in range(int(input()))]

print(solve(turtle_statements))
