import heapq


# Initial state
initial = (2, 8, 3,
           1, 6, 4,
           7, 0, 5)

# Goal state
goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Print the state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Generate possible moves
def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


# ------------------------------------------------
# CASE 1: MISPLACED TILES
# Blank is also counted
# ------------------------------------------------

def misplaced_tiles(state):

    count = 0

    for i in range(9):

        if state[i] != goal[i]:
            count += 1

    return count


# ------------------------------------------------
# CASE 2: MANHATTAN DISTANCE
# Blank is also counted
# ------------------------------------------------

def manhattan_distance(state):

    distance = 0

    for i in range(9):

        if state[i] != goal[i]:

            current_row = i // 3
            current_col = i % 3

            goal_position = goal.index(state[i])

            goal_row = goal_position // 3
            goal_col = goal_position % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# ------------------------------------------------
# A* SEARCH
# ------------------------------------------------

def a_star(heuristic):

    open_list = []

    g_value = {initial: 0}

    parent = {initial: None}

    counter = 0

    h = heuristic(initial)

    f = h

    heapq.heappush(
        open_list,
        (f, counter, initial)
    )

    closed = set()

    while open_list:

        f, _, current = heapq.heappop(open_list)

        if current in closed:
            continue

        closed.add(current)

        # Goal test
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path

        # Generate successors
        for neighbor in get_neighbors(current):

            if neighbor in closed:
                continue

            new_g = g_value[current] + 1

            if neighbor not in g_value or new_g < g_value[neighbor]:

                g_value[neighbor] = new_g

                parent[neighbor] = current

                h = heuristic(neighbor)

                f = new_g + h

                counter += 1

                heapq.heappush(
                    open_list,
                    (f, counter, neighbor)
                )

    return None


# ------------------------------------------------
# DISPLAY TRACING
# ------------------------------------------------

def display_solution(path, heuristic):

    print("------------------------------------")
    print("A* SEARCH")
    print("------------------------------------")

    for step, state in enumerate(path):

        g = step

        h = heuristic(state)

        f = g + h

        print("Step:", step)

        print_state(state)

        print("g(n) =", g)
        print("h(n) =", h)
        print("f(n) =", f)

        print("------------------------------------")

    print("Total moves =", len(path) - 1)


# ------------------------------------------------
# CASE 1
# ------------------------------------------------

print("\nCASE 1: MISPLACED TILES\n")

path1 = a_star(misplaced_tiles)

display_solution(path1, misplaced_tiles)


# ------------------------------------------------
# CASE 2
# ------------------------------------------------

print("\nCASE 2: MANHATTAN DISTANCE\n")

path2 = a_star(manhattan_distance)

display_solution(path2, manhattan_distance)