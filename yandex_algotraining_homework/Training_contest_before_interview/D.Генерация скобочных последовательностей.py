# https://contest.yandex.ru/contest/8458/

def gen(cur,opened,closed,n):
    if len(cur) == 2*n: print(cur); return

    if opened < n: gen(cur+"(",opened+1,closed,n)

    if closed < opened: gen(cur+")",opened,closed+1,n)

gen("",0,0,int(input()))
