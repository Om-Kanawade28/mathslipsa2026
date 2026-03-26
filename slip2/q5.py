graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def bfs(start, goal):
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        for n in graph[node]:
            queue.append(path + [n])

print("Shortest Path:", bfs('A', 'E'))