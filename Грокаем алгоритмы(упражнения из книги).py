# Реализация самостоятельных упражнений из книги "Грокаем алгоритмы".


def sum(arr):
    if not arr: return 0
    else: return arr[0] + sum(arr[1:])


assert sum([2,4,6]) == 12


def nod(a, b):
    if a == 0: return b
    elif b == 0: return a
    else: return nod(b, a % b)


assert nod(1680,640) == 80


def max(arr):
    m = arr[0]

    for n in arr:
        if n > m: m = n

    return m


assert max([4,5,11,6]) == 11


def bin_search(arr, l, r, target):
    if l <= r:
        m = (l+r) // 2; guess = arr[m]

        if guess == target: return m
        elif guess > target: return bin_search(arr,l,m-1,target)
        else: return bin_search(arr,m+1,r,target)

    else: return -1


assert bin_search([1, 3, 5, 7, 9, 43, 645, 43325, 63262346],0,9,43325) == 7


def choice_sort(arr):
    res = []

    while arr:
        min, min_idx = arr[0], 0

        for i, v in enumerate(arr):
            if v < min: min = v; min_idx = i

        res.append(arr.pop(min_idx))

    return res


assert choice_sort([1, 63262346, 3, 5, 7, 9, 645, 43325, 43]) == [1, 3, 5, 7, 9, 43, 645, 43325, 63262346]


def quick_sort(arr):
    if len(arr) < 2: return arr
    else:
        pivot, less, greater = arr.pop(), [], []

        for n in arr:
            if n < pivot: less.append(n)
            else: greater.append(n)

    return quick_sort(less) + [pivot] + quick_sort(greater)


assert quick_sort([1, 63262346, 3, 5, 7, 9, 645, 43325, 43]) == [1, 3, 5, 7, 9, 43, 645, 43325, 63262346]


from collections import deque
# Поиск в ширину
graph = {"you": ["alice","bob","claire"]}
graph["bob"] = ["anuj", "peggy"]; graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]; graph["anuj"] = []
graph["peggy"] = []; graph["thom"] = []; graph["jonny"] = []

def is_seller(name): return name[-1] == "m"

def bfs(graph):
    deq, seen = deque(), set(); deq += graph["you"]

    while deq:
        person = deq.popleft()

        if not person in seen:  
            if is_seller(person): return person
            else: deq += graph[person]; seen.add(person)

    return False


assert bfs(graph) == "thom"


from collections import defaultdict
# Алгоритм Дейкстры
graph = defaultdict(lambda:defaultdict(int))
graph["start"]["a"] = 6; graph["start"]["b"] = 2
graph["a"]["fin"] = 1; graph["b"]["a"] = 3
graph["b"]["fin"] = 5

costs = defaultdict(int)
costs["a"] = 6; costs["b"] = 2
costs["fin"] = float("inf")

parents = defaultdict(str)
parents["a"] = "start"; parents["b"] = "start"
parents["fin"] = float("inf")

processed = set()

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost; lowest_cost_node = node
    
    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors:
        new_cost = cost + neighbors[n]

        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    
    processed.add(node)
    node = find_lowest_cost_node(costs)

assert costs["fin"] == 6
