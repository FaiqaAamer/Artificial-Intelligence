# Tree from your diagram
graph = {
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

def dfs_using_stack(graph, start, goal):
    stack = [start] # Stack for DFS - We start with A inside it 
    visited = set() # To remember which node is visited
    traversal_order = [] # Order in which nodes are visited

    print(f"Start Node: {start}, Goal Node: {goal}\n")

    while stack:
        # Pop from stack (LIFO)
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        traversal_order.append(current)

        print(f"Visited: {current} | Stack: {stack} | Traversal: {traversal_order}")

        # Check goal
        if current == goal:
            print(f"\nGOAL FOUND: {goal}")
            return traversal_order

        # Push children in reverse order to visit left child first
        # e.g., if children are [B, F, D, E], push as [E, D, F, B]
        # so B is popped first
        children = graph.get(current, [])
        for child in reversed(children):
            if child not in visited:
                stack.append(child)

    print("\nGoal not found")
    return traversal_order

# Run
start = 'A'
goal = 'G'
result = dfs_using_stack(graph, start, goal)

print(f"\nFinal DFS Traversal Order: {result}")

graph = {
    1: [2, 7, 8],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [9, 12],
    9: [10, 11],
    10: [],
    11: [],
    12: []
}


def dfs(graph, start, goal):

    stack = [start]
    visited = []

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.append(node)

            print("Visiting:", node)

            if node == goal:
                print("Goal node found:", goal)
                return

            for neighbor in reversed(graph[node]):

                if neighbor not in visited:
                    stack.append(neighbor)

    print("Goal node not found")


dfs(graph, 1, 12)