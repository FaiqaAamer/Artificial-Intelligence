####1.BFS on given graph


# Graph represented using adjacency list
graph1 = {
    0: [1, 4],
    1: [0, 4, 3, 2],
    2: [1, 3],
    3: [1, 4, 2],
    4: [0, 1, 3]
}

graph2 = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

def bfs(graph, start):
    

    # Add starting node to queue
    queue=[start]
    visited=[start]

    print("\nBFS Traversal:")

    while queue:
        # Remove first element from queue
        node = queue.pop(0)

        print(node, end=" ")

        # Visit all neighbours
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Start BFS from node 0
bfs(graph1, 0)
bfs(graph2, 2)


####2.BFS from A to goal G
# Tree represented using adjacency list
tree = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}

def bfs(tree, start, goal):
    queue = [start]
    visited = [start]
    print("\nBFS SEARCH:")

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!", node)
            return

        for neighbour in tree[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    print("\nGoal not found!")

bfs(tree, 'A', 'G')





####3.implementing priority queue
import heapq

# Create an empty priority queue
priority_queue = []

# Add elements
heapq.heappush(priority_queue, (3, "Task C"))
heapq.heappush(priority_queue, (1, "Task A"))
heapq.heappush(priority_queue, (2, "Task B"))
heapq.heappush(priority_queue, (5, "Task E"))
heapq.heappush(priority_queue, (4, "Task D"))

print("Priority Queue:")

# Remove elements according to priority
while priority_queue:
    priority, task = heapq.heappop(priority_queue)

    print("Priority:", priority, "| Task:", task)