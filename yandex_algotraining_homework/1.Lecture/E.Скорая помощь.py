# https://contest.yandex.ru/contest/27393/enter/

def get_p_n(k, fs, apparts_floor):
    p = (k - 1) // (apparts_floor * fs) + 1
    n = (k - (p - 1) * apparts_floor * fs - 1) // apparts_floor + 1

    return p, n

def decision(k1, fs, k2, p2, f2):
    offset = (p2 - 1) * fs + (f2 - 1) # Смещение в этажах для k2-квартиры
    apparts_floor_max = (k2 - 1) // offset # Предположиттельное максимальное значение квартир на этаж 
    apparts_floor_min = (k2 - 1) // (offset + 1) + 1 # Предположительное минимальное значение квартир на этаж

    if apparts_floor_max == 0 or (k2 - 1) // apparts_floor_max != offset: return -1, -1 # Проверим верно ли полученное значение квартир на этаже

    if (k2 - 1) // apparts_floor_min != offset: apparts_floor_max = apparts_floor_min # Если не корректное значение, запишем в него корректное значение
    
    p1_1, n1_1 = get_p_n(k1, fs, apparts_floor_min) # Вычислили возможные значения p и т для разных значений квартир на этаже
    p1_2, n1_2 = get_p_n(k1, fs, apparts_floor_max)

    return 0 if p1_1 != p1_2 else p1_1, 0 if n1_1 != n1_2 else n1_1


k1, fs, k2, p2, f2 = map(int, input().split())

if f2 > fs: print(-1, -1) # Номер этажа не может быть больше их количества в доме
elif f2 == 1 and p2 == 1:# Если у известной квартиры первый подъезд и первый этаж, то можно сразу дать ответ
    if k1 > k2: print(1 if k1 <= fs else 0, 1 if fs == 1 else 0)
    else: print(p2, f2)
else: print(*decision(k1, fs, k2, p2, f2))
