map_rooms = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["G"],
    "G": []
}

door_costs = {
    ("A", "B"): 1,
    ("B", "D"): 1,
    ("A", "C"): 5,
    ("C", "D"): 1,
    ("D", "G"): 1
}


def bfs(start, goal):
    queue = [(start, [start])]
    visited = []

    while queue:
        room, path = queue.pop(0)

        if room in visited:
            continue

        visited.append(room)

        if room == goal:
            return path, visited

        for next_room in map_rooms[room]:
            queue.append((next_room, path + [next_room]))

    return [], visited


def dfs(start, goal):
    stack = [(start, [start])]
    visited = []

    while stack:
        room, path = stack.pop()

        if room in visited:
            continue

        visited.append(room)

        if room == goal:
            return path, visited

        for next_room in reversed(map_rooms[room]):
            stack.append((next_room, path + [next_room]))

    return [], visited


def path_cost(path):
    total = 0

    for i in range(len(path) - 1):
        total += door_costs[(path[i], path[i + 1])]

    return total


start = "A"
goal = "G"

bfs_path, bfs_order = bfs(start, goal)
dfs_path, dfs_order = dfs(start, goal)

bfs_cost = path_cost(bfs_path)
dfs_cost = path_cost(dfs_path)

print("BFS")
print("Path:", bfs_path)
print("Cost:", bfs_cost)
print("Rooms checked:", bfs_order)
print("Number of rooms:", len(bfs_order))

print("\nDFS")
print("Path:", dfs_path)
print("Cost:", dfs_cost)
print("Rooms checked:", dfs_order)
print("Number of rooms:", len(dfs_order))

print("\nComparison")

if bfs_cost < dfs_cost:
    print("BFS has lower path cost")
elif dfs_cost < bfs_cost:
    print("DFS has lower path cost")
else:
    print("Both have the same path cost")

print("\nCheapest Path")

paths = [bfs_path, dfs_path]
costs = [bfs_cost, dfs_cost]

best_index = costs.index(min(costs))

print("Path:", paths[best_index])
print("Cost:", costs[best_index])