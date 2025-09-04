import random

def print_board(board):
    """prints the board and Shows the board positions for reference """
    for i in range(3):
        print(f"{board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]}")
        if i < 2:  # print separator line after rows 0 and 1 only
            print("--+---+--")


# check if player has won

def check_for_winner(board):
    """ Checks if winning patterns on rows, columns or diagonals"""
    winning_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonal
    ]
    for line in winning_patterns:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]
    return None  # if no one wins


def full_board(board):
    """Checks if no empty spaces remain"""
    return " " not in board


def tic_tac_toe():
    board = [" "] * 9  # create list of empty strings
    current_player = "X"  # assign X to first player
    print("Welcome to text-based Tic Tac Toe")
    print("Enter a number (1-9) to place your mark")
    print_board([str(i + 1) for i in range(9)])
    print("\n Let's Begin\n")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        if current_player == 'O': # AI's turn
            empty_positions = [i for i, spot in enumerate(board) if spot == " "]
            position = random.choice(empty_positions)
            print(f" AI chooses position {position + 1 }")
        else: # real players' turn
            try:
                position = int(input("Choose position (1-9)")) - 1
                if position < 0 or position > 8:
                    print('Please enter a number between (1-9)')
                    continue

                if board[position] != " ":  # check for empty position
                    print("That position is already taken")
                    continue
            except ValueError:
                print("Invalid input, please Enter a number")
                continue
        # Place the move
        board[position] = current_player
        # check for winner
        winner = check_for_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} Wins!!🏆")
            break
        if full_board(board):
            print_board(board)
            print("It's a Tie!! 🎀")

        current_player = 'O' if current_player == "X" else 'X'


if __name__ == "__main__":
    tic_tac_toe()
