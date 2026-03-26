graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

visited = []

def bfs(start):
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node in visited:
            return True   # cycle found

        visited.append(node)
        queue.extend(graph[node])

    return False

print("Cycle Detected:", bfs('A'))