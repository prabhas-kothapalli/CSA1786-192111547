import heapq

tree = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'E': 1},
    'E': {}
}

heuristics = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 0,
    'E': 0
}

def f(current, goal, cost):
    return cost + heuristics[goal]

def a_star_search(graph, start, goal):
    frontier = [(0, start)]
    path = []
    visited = set()
    while frontier:
        cost, current = heapq.heappop(frontier)
        if current == goal:
            return path
        visited.add(current)
        for neighbor, cost2 in graph[current].items():
            if neighbor not in visited:
                total_cost = cost + cost2
                heapq.heappush(frontier, (f(neighbor, goal, total_cost), neighbor))
                path.append((current, neighbor, total_cost))
    return None

result = a_star_search(tree, 'A', 'E')
print(result)
