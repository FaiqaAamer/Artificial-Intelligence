# Graph representation (Adjacency List)
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'C': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'F': [],
    'G': [],
    'H': [],
    'I': ['L'],
    'J': [],
    'K': ['N', 'M'],
    'L': [],
    'M': [],
    'N': []
}

# Depth Limited Search (DLS)
def DLS(node, target, limit):
    if node == target:
        return [node]  # Found target, return path
    if limit <= 0:
        return None    # Cutoff depth reached
    
    for child in graph.get(node, []):
        path = DLS(child, target, limit - 1)
        if path:
            return [node] + path
    return None

# Iterative Deepening Depth First Search (IDDFS)
def IDDFS(start, target, max_depth):
    for depth in range(max_depth + 1):
        path = DLS(start, target, depth)
        if path:
            return path
    return None

# Run searches
goal = 'G'
print("DLS (limit=3):", DLS('A', goal, 3))
print("IDDFS (max_depth=5):", IDDFS('A', goal, 5))
