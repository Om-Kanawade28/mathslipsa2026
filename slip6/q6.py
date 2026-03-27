graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

visited = []
stack = []

def dfs(node):
    visited.append(node)
    stack.append(node)

    for nei in graph[node]:
        if nei not in visited:
            if dfs(nei):
                return True
        elif nei in stack:
            return True   # cycle found

    stack.remove(node)
    return False

# check cycle
print("Cycle Detected:", dfs('A'))