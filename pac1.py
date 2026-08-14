from collections import deque

graph = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 1)],
    "C": [("D", 1)],
    "D": [("G", 1)],
    "G": []
}


def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()

    while queue:
        node, path, cost = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost, visited

        for next_node, edge_cost in graph[node]:
            queue.append(
                (next_node, path + [next_node], cost + edge_cost)
            )

    return [], 0, visited


def dfs(start, goal):
    stack = [(start, [start], 0)]
    visited = set()

    while stack:
        node, path, cost = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost, visited

        for next_node, edge_cost in reversed(graph[node]):
            stack.append(
                (next_node, path + [next_node], cost + edge_cost)
            )

    return [], 0, visited


start = "A"
goal = "G"

bfs_path, bfs_cost, bfs_visited = bfs(start, goal)
dfs_path, dfs_cost, dfs_visited = dfs(start, goal)

print("BFS")
print("Path:", " -> ".join(bfs_path))
print("Path Cost:", bfs_cost)
print("Rooms Checked:", list(bfs_visited))
print("Number of Rooms:", len(bfs_visited))

print("\nDFS")
print("Path:", " -> ".join(dfs_path))
print("Path Cost:", dfs_cost)
print("Rooms Checked:", list(dfs_visited))
print("Number of Rooms:", len(dfs_visited))

print("\nComparison")

if bfs_cost < dfs_cost:
    print("BFS has lower path cost")
elif dfs_cost < bfs_cost:
    print("DFS has lower path cost")
else:
    print("Both have the same path cost")