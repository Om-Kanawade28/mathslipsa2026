import math

cities = [(0,0), (1,2), (4,0)]

visited = [0]
current = 0

while len(visited) < len(cities):
    nearest = None
    min_dist = 999

    for i in range(len(cities)):
        if i not in visited:
            d = math.dist(cities[current], cities[i])
            if d < min_dist:
                min_dist = d
                nearest = i

    visited.append(nearest)
    current = nearest

print("Path:", visited)