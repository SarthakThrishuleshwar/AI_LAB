# Iterative Deepening Search for 8-Puzzle
# 0 represents the blank space


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Generate all possible moves
def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Up
    if row > 0:
        new_state = list(state)

        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]

        neighbors.append(("Up", tuple(new_state)))

    # Down
    if row < 2:
        new_state = list(state)

        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]

        neighbors.append(("Down", tuple(new_state)))

    # Left
    if col > 0:
        new_state = list(state)

        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]

        neighbors.append(("Left", tuple(new_state)))

    # Right
    if col < 2:
        new_state = list(state)

        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]

        neighbors.append(("Right", tuple(new_state)))

    return neighbors


# Depth Limited DFS
def depth_limited_search(state, goal, limit, path, moves):

    # Goal test
    if state == goal:
        return path, moves

    # Depth limit reached
    if limit == 0:
        return None

    # Explore successors
    for move, next_state in get_neighbors(state):

        # Avoid states already present in current path
        if next_state not in path:

            path.append(next_state)
            moves.append(move)

            result = depth_limited_search(
                next_state,
                goal,
                limit - 1,
                path,
                moves
            )

            if result is not None:
                return result

            # Backtrack
            path.pop()
            moves.pop()

    return None


# Iterative Deepening Search
def iterative_deepening_search(start, goal, max_depth=50):

    for depth in range(max_depth + 1):

        print("Searching at depth:", depth)

        path = [start]
        moves = []

        result = depth_limited_search(
            start,
            goal,
            depth,
            path,
            moves
        )

        if result is not None:
            return result

    return None


# --------------------------------
# Main Program
# --------------------------------

initial = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


print("INITIAL STATE")
print_board(initial)

print("GOAL STATE")
print_board(goal)


result = iterative_deepening_search(
    initial,
    goal
)


if result is not None:

    path, moves = result

    print("\n========================")
    print("SOLUTION FOUND")
    print("========================")

    print("\nMoves:")
    print(" -> ".join(moves))

    print("\nNumber of moves:", len(moves))

    print("\nSolution Path:")

    for i, state in enumerate(path):

        print("Step", i)
        print_board(state)

else:

    print("No solution found.")