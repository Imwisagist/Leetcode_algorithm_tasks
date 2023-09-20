# https://contest.yandex.ru/contest/27472/enter/

def solve():
    END = -2000000000; prev = type = None

    while True:
        number = int(input())

        if number == END or type == 'RANDOM': break

        if prev:
            if number == prev:
                if not type: type = 'CONSTANT'
                elif type == 'ASCENDING': type = 'WEAKLY ASCENDING'
                elif type == 'DESCENDING': type = 'WEAKLY DESCENDING'
            elif number > prev:
                if not type: type = 'ASCENDING'
                elif type == 'WEAKLY DESCENDING' or type == 'DESCENDING': type = 'RANDOM'
                elif type == 'CONSTANT': type = 'WEAKLY ASCENDING'
            else: 
                if not type: type = 'DESCENDING'
                elif type == 'WEAKLY ASCENDING' or type == 'ASCENDING': type = 'RANDOM'
                elif type == 'CONSTANT': type = 'WEAKLY DESCENDING'

        prev = number
        
    return type


print(solve())
