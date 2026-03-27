#  Write a Python Program to find all nodes reachable from a given source using BFS in a    
#     directed graph.. 
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}
def bfs(start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node  not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
result = bfs('A')
print("Nodes reachable form A:", result)
print("Nodes reachable form B:", bfs('B'))