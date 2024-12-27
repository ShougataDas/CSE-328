import heapq

def greedy_best_first_search(graph, start, goal, heuristics):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start], start))

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current in visited:
            continue
        print(f"Visited: {current}")
        visited.add(current)

        if current == goal:
            print("Goal reached!")
            return True

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

    print("Goal not reachable!")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristics = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 0}
start = 'A'
goal = 'F'

greedy_best_first_search(graph, start, goal, heuristics)
