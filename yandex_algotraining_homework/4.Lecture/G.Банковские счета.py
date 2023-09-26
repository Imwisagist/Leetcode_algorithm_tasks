# https://contest.yandex.ru/contest/27665/enter/

import sys

def solve(data):
    def income(percent):
        for person,amount in d.items():
            if amount > 0: d[person] = int(amount*percent//100) + amount

    def transfer(from_,to_,amount): withdraw(from_,amount); deposit(to_,amount)

    def deposit(name,amount): d[name] = d_get(name,0) + amount

    def withdraw(name,amount): d[name] = d_get(name,0) - amount

    operations = {
        "DEPOSIT": lambda name,amount: deposit(name,int(amount)),
        "INCOME": lambda percent: income(int(percent)),
        "BALANCE": lambda name: print(d_get(name,"ERROR")),
        "TRANSFER": lambda from_,to_,amount: transfer(from_,to_,int(amount)),
        "WITHDRAW": lambda name,amount: withdraw(name,int(amount)),
    }; d = {}; d_get = d.get

    for operation,*other in data: operations[operation](*other)


solve([d.split() for d in sys.stdin])
