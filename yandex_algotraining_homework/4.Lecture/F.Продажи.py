# https://contest.yandex.ru/contest/27665/enter/

from collections import defaultdict
import sys

def solve(data):
    d = defaultdict(lambda: defaultdict(int))

    for name,product,count in data:
        d[name][product] += int(count)

    for name,products in sorted(d.items()):
        print(name+":")

        for product,count in sorted(products.items()):
            print(product,count)


solve([d.split() for d in sys.stdin])
