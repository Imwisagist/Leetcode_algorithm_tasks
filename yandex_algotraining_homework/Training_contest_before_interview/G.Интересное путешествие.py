# https://contest.yandex.ru/contest/8458/

def get_distance(c1,c2): return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])

def bfs(paths,a,b):
    distance = [-1] * len(paths); distance[a],towns = 0,[a]

    while towns:
        path = towns.pop(0)

        for town in paths[path]:
            if distance[town] == -1: towns.append(town); distance[town] = distance[path] + 1

    return distance[b]

def get_path_length(cities,k,start,end):
    if get_distance(cities[start],cities[end]) <= k: return 1

    tracks = [
        [
            idx
            for idx, city2 in enumerate(cities)
            if get_distance(city1,city2) <= k
        ]
        for city1 in cities
    ]
        
    return bfs(tracks,start,end)


n = int(input()); cities = [tuple(map(int,input().split())) for _ in range(n)]
k = int(input()); start,end = [int(i) - 1 for i in input().split()]

print(get_path_length(cities,k,start,end))
