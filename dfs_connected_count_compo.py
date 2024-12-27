visited = set()
graph = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B'},
    'D': {'E'},
    'E': {'D'}
}

component = int(0)

def dfs(node):
    global component
    if node not in visited:
        visited.add(node)
        for child in graph[node]:
            component+=1
            dfs(child)

component_list = []
for key in graph:
    if key not in visited:
        dfs(key)
        component_list.append(component)
        component = 0

sz = len(component_list)

if sz > 1:
    print("Not Connected")
else:
    print("Connected")

print(f"Number of component: {component_list}")