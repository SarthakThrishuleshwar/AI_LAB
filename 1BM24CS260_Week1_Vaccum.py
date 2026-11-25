
def dfs_8_puzzle(start, goal):
    # Stack stores states to explore
    stack = [start]

    # Track visited states to avoid cycles
    visited = {start}

    # Store parent state and move used to reach each state
    parent = {start: (None, None)}

    expanded = 0

    while stack:
        current = stack.pop()
        expanded += 1

        # Print the first few expanded states
        if expanded <= 10:
            print(f"\nExpanded state {expanded}:")
            print_board(current)

        # Check whether the goal is reached
        if current == goal:
            print("\nGoal state reached!")
            print("Total states expanded:", expanded)

            # Reconstruct the path
            path = []
            moves = []
            state = current

            while state is not None:
                path.append(state)
                previous, move = parent[state]

                if previous is not None:
                    moves.append(move)

                state = previous

            path.reverse()
            moves.reverse()

            print("\nSolution path:")
            for i, state in enumerate(path):
                print(f"\nStep {i}:")
                print_board(state)

                if i < len(moves):
                    print("Move:", moves[i])

            print("\nTotal moves:", len(moves))
            return path

        # Find the blank tile (0)
        blank = current.index(0)
        row, col = divmod(blank, 3)

        # Move order: Up, Down, Left, Right
        directions = [
            ("Up", -1, 0),
            ("Down", 1, 0),
            ("Left", 0, -1),
            ("Right", 0, 1)
        ]

        neighbors = []

        for move, dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            # Check board boundaries
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_blank = new_row * 3 + new_col

                board = list(current)

                # Swap blank with adjacent tile
                board[blank], board[new_blank] = (
                    board[new_blank], board[blank]
                )

                next_state = tuple(board)
                neighbors.append((move, next_state))

        # Reverse insertion so DFS explores the
        # specified move order when popping the stack
        for move, next_state in reversed(neighbors):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (current, move)
                stack.append(next_state)

    print("No solution found.")
    return None


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])


# 0 represents the blank tile
initial_state = (5, 4, 0,
                 6, 1, 8,
                 7, 3, 2)

goal_state = (0, 1, 2,
              3, 4, 5,
              6, 7, 8)

dfs_8_puzzle(initial_state, goal_state)