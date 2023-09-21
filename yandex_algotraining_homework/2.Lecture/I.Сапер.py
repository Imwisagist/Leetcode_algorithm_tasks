# https://contest.yandex.ru/contest/27472/enter/

def solve(n, m, k):
    mines = [tuple(map(int, input().split())) for _ in range(k)]
    nbrs_ofst_x = (-1,-1,-1,0,0,1,1,1)
    nbrs_ofst_y = (-1,0,1,-1,1,-1,0,1)
    field = [[0] * (m + 2) for _ in range(n + 2)]

    for m_x, m_y in mines:
        for i in range(len(nbrs_ofst_x)):
            field[m_x + nbrs_ofst_x[i]][m_y + nbrs_ofst_y[i]] += 1
        
    for m_x, m_y in mines: field[m_x][m_y] = "*"

    for i in range(1, n + 1):
        print(*(field[i][j] for j in range(1, m + 1)))
        

n, m, k = map(int, input().split())

solve(n, m, k)
