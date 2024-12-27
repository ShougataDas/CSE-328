from collections import deque
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
obstacles = {'E'}
visited = set()
queue = deque(['A'])
while queue:
    node = queue.popleft()
    if node not in visited and node not in obstacles:
        visited.add(node)
        queue.extend(graph[node] - visited)

for key,value in graph.items():
    if key in visited:
        print(f"{key} is visited")
    else:
        print(f"{key} is obstacle and is not visited")


