# Tic-Tac-Toe: Human vs Computer

board = [' ' for _ in range(9)]


def display_board():
    print()
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),  # Row 1
        (3, 4, 5),  # Row 2
        (6, 7, 8),  # Row 3
        (0, 3, 6),  # Column 1
        (1, 4, 7),  # Column 2
        (2, 5, 8),  # Column 3
        (0, 4, 8),  # Diagonal
        (2, 4, 6)   # Diagonal
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def board_full():
    return ' ' not in board


def computer_move():
    # Computer tries to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner('O'):
                return
            board[i] = ' '

    # Computer tries to block the human
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner('X'):
                board[i] = 'O'
                return
            board[i] = ' '

    # Take the center if available
    if board[4] == ' ':
        board[4] = 'O'
        return

    # Take any available position
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            return


# Main game
print("===== TIC-TAC-TOE =====")
print("Human = X")
print("Computer = O")

while True:
    display_board()

    # Human's turn
    while True:
        try:
            position = int(input("Enter your position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
            elif board[position - 1] != ' ':
                print("That position is already occupied.")
            else:
                board[position - 1] = 'X'
                break

        except ValueError:
            print("Please enter a valid number.")

    # Check human win
    if check_winner('X'):
        display_board()
        print("Congratulations! HUMAN wins!")
        break

    # Check draw
    if board_full():
        display_board()
        print("The game is a DRAW!")
        break

    # Computer's turn
    print("Computer's turn...")
    computer_move()

    # Check computer win
    if check_winner('O'):
        display_board()
        print("COMPUTER wins!")
        break

    # Check draw
    if board_full():
        display_board()
        print("The game is a DRAW!")
        break