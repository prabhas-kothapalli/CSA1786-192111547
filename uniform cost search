import heapq

def uniform_cost_search(graph, start, goal):
    
    queue = [(0, start)]
    visited = set()

    while queue:
        (cost, current) = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return cost
        for neighbor in graph[current]:
            
            new_cost = cost + graph[current][neighbor]
            heapq.heappush(queue, (new_cost, neighbor))

    return None
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'C': 3},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {'G': 2},
}

print(uniform_cost_search(graph, 'S', 'G')) 
