# https://contest.yandex.ru/contest/51022/enter/

from datetime import datetime, time

days_in_month = (31,28,31,30,31,30,31,31,30,31,30,31)

def count_the_number_of_days(year: int,month: int,day: int) -> int:
    count_days = (year-1) * 365 + day

    for m in range(month-1): count_days += days_in_month[m]

    return count_days

begin = datetime(*map(int,input().split()))
end = datetime(*map(int,input().split()))
time1 = time(begin.hour,begin.minute,begin.second)
time2 = time(end.hour,end.minute,end.second)
days1 = count_the_number_of_days(begin.year,begin.month,begin.day)
days2 = count_the_number_of_days(end.year,end.month,end.day)

if time2 < time1: print(days2-days1-1,(end-begin).seconds)
else: print(days2-days1,(end-begin).seconds)
