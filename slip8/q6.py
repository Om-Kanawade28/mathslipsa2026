graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for nei in graph[node]:
            dfs(nei)

# Start DFS
print("DFS Traversal:")
dfs('A')