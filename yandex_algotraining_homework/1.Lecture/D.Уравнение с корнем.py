# https://contest.yandex.ru/contest/27393/enter/

def decision(a, b, c):
	if c < 0: return "NO SOLUTION"
	elif a == 0 and b == c**2: return "MANY SOLUTIONS"
	else:
		n = c**2 - b
		if a != 0 and n / a == n // a: return n // a
		else: return "NO SOLUTION"

a, b, c = int(input()), int(input()), int(input())

print(decision(a,b,c))
