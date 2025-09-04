import random


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def print_board(self):
        for i in range(3):
            print(f"{self.board[i * 3]} | {self.board[i * 3 + 1]} | {self.board[i * 3 + 2]}")
            if i < 2:
                print("--+---+--")

    def print_board_numbers(self):
        for i in range(3):
            print(f"{i * 3 + 1} | {i * 3 + 2} | {i * 3 + 3}")
            if i < 2:
                print("--+---+--")

    def check_for_winner(self):
        winning_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for line in winning_patterns:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return self.board[line[0]]
        return None

    def full_board(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == "X" else 'X'

    # Smarter AI
    def ai_choose_move(self):
        empty_positions = [i for i, spot in enumerate(self.board) if spot == " "]

        # 1. Win if possible
        for pos in empty_positions:
            self.board[pos] = 'O'
            if self.check_for_winner() == 'O':
                return pos
            self.board[pos] = " "

        # 2. Block player from winning
        for pos in empty_positions:
            self.board[pos] = 'X'
            if self.check_for_winner() == 'X':
                self.board[pos] = " "
                return pos
            self.board[pos] = " "

        # 3. Take center
        if 4 in empty_positions:
            return 4

        # 4. Take a corner
        corners = [i for i in [0, 2, 6, 8] if i in empty_positions]
        if corners:
            return random.choice(corners)

        # 5. Take a side
        sides = [i for i in [1, 3, 5, 7] if i in empty_positions]
        if sides:
            return random.choice(sides)

        # fallback
        return random.choice(empty_positions)

    def play_game(self):
        print("Welcome to text-based Tic Tac Toe")
        print("Enter a number (1-9) to place your mark")
        self.print_board_numbers()
        print("\nLet's Begin\n")

        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")

            if self.current_player == 'O':  # AI's turn
                position = self.ai_choose_move()
                print(f"AI chooses position {position + 1}")
            else:
                try:
                    position = int(input("Choose position (1-9)")) - 1
                    if position < 0 or position > 8:
                        print("Please enter a number between 1-9")
                        continue
                    if self.board[position] != " ":
                        print("That position is already taken")
                        continue
                except ValueError:
                    print("Invalid input, please enter a number")
                    continue

            # Record the move
            self.board[position] = self.current_player

            # Check for winner
            winner = self.check_for_winner()
            if winner:
                self.print_board()
                print(f"Player {winner} Wins!! 🏆")
                break

            if self.full_board():
                self.print_board()
                print("It's a Tie!! 🎀")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
