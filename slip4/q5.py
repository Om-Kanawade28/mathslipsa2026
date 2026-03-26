# Graph (directed)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def bfs_path_exists(start, goal):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node == goal:
            return True

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return False

# Test
print(bfs_path_exists('A', 'E'))   # True