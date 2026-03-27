V = 4
edges = [(0,1,5), (1,2,3)]   # 3 is unreachable

dist = [999]*V
dist[0] = 0   # source

# Relax edges
for i in range(V-1):
    for u,v,w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

# Print result
for i in range(V):
    if dist[i] == 999:
       print("Vertex", i, "is unreachable")
    else:
         print("Distance to", i, "=", dist[i])