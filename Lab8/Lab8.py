import heapq

# ---------------- Map data (Bucharest map from the lab) ----------------
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
}

# Straight-line distance to Bucharest (heuristic h)
h = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374,
}


# ---------------- Task 1: Greedy Best First Search  f(n) = h(n) ----------------
def greedy(start, goal):
    open_list = [(h[start], start, [start])]   # (h, city, path)
    closed = set()
    while open_list:
        _, city, path = heapq.heappop(open_list)
        if city == goal:
            return path
        if city in closed:
            continue
        closed.add(city)
        for nxt in graph[city]:
            if nxt not in closed:
                heapq.heappush(open_list, (h[nxt], nxt, path + [nxt]))
    return None


# ---------------- Task 2: A* Search  f(n) = g(n) + h(n) ----------------
def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]   # (f, g, city, path)
    closed = set()
    while open_list:
        f, g, city, path = heapq.heappop(open_list)
        if city == goal:
            return path, g
        if city in closed:
            continue
        closed.add(city)
        for nxt, cost in graph[city].items():
            if nxt not in closed:
                g2 = g + cost
                heapq.heappush(open_list, (g2 + h[nxt], g2, nxt, path + [nxt]))
    return None, None


# ---------------- Task 3: 8 Puzzle using A* ----------------
# State = tuple of 9 numbers, 0 means the empty space
def misplaced(state, goal):
    # heuristic: number of tiles not in the right place
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])


def neighbors(state):
    result = []
    i = state.index(0)            # position of the blank
    row, col = i // 3, i % 3
    moves = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
    for name, (dr, dc) in moves.items():
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            s = list(state)
            s[i], s[j] = s[j], s[i]   # slide the tile into the blank
            result.append((name, tuple(s)))
    return result


def puzzle_astar(start, goal):
    open_list = [(misplaced(start, goal), 0, start, [])]  # (f, g, state, moves)
    closed = set()
    while open_list:
        f, g, state, moves = heapq.heappop(open_list)
        if state == goal:
            return moves
        if state in closed:
            continue
        closed.add(state)
        for move, nxt in neighbors(state):
            if nxt not in closed:
                g2 = g + 1
                heapq.heappush(open_list,
                               (g2 + misplaced(nxt, goal), g2, nxt, moves + [move]))
    return None


def show(state):
    for r in range(3):
        print(' '.join(str(x) if x != 0 else '_' for x in state[r*3:r*3+3]))
    print()


# ---------------- Run everything ----------------
if __name__ == '__main__':
    print("=== Task 1: Greedy Best First Search (Arad -> Bucharest) ===")
    print(" -> ".join(greedy('Arad', 'Bucharest')))

    print("\n=== Task 2: A* Search (Arad -> Bucharest) ===")
    path, cost = astar('Arad', 'Bucharest')
    print(" -> ".join(path))
    print("Total cost:", cost)

    print("\n=== Task 3: 8 Puzzle using A* ===")
    start = (1, 2, 3,
             5, 6, 0,
             7, 8, 4)
    goal = (1, 2, 3,
            5, 8, 6,
            0, 7, 4)
    print("Start:")
    show(start)
    print("Goal:")
    show(goal)
    moves = puzzle_astar(start, goal)
    if moves is None:
        print("No solution found")
    else:
        print("Moves of the blank space:", moves)
        print("Number of moves:", len(moves))
        state = start
        for m in moves:
            for name, nxt in neighbors(state):
                if name == m:
                    state = nxt
                    break
            print("Move", m)
            show(state)
