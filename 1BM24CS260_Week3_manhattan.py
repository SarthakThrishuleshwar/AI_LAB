
def calculate_cost(state):
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


def hill_climbing(state):
    step = 0

    while True:
        current_cost = calculate_cost(state)

        print("Step:", step)
        print("State:", state)
        print("Cost:", current_cost)
        print()

        if current_cost == 0:
            print("Solution Found!")
            return state

        best_state = state[:]
        best_cost = current_cost

        for i in range(4):
            for j in range(i + 1, 4):
                neighbor = state[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

                cost = calculate_cost(neighbor)

                if cost < best_cost:
                    best_cost = cost
                    best_state = neighbor

        if best_cost >= current_cost:
            print("No better neighbor found!")
            return None

        state = best_state
        step += 1


# Main Program
initial_state = [3, 1, 2, 0]

result = hill_climbing(initial_state)

if result is not None:
    print("Final Solution:", result)
else:
    print("Solution not found")
