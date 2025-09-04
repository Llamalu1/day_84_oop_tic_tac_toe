import random


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def print_board(self):  # Prints the empty board
        for i in range(3):
            print(f"{self.board[i * 3]} | {self.board[i * 3 + 1]} | {self.board[i * 3 + 2]}")
            if i < 2:  # print separator line after rows 0 and 1 only
                print("--+---+--")

    def print_board_numbers(self):
        """Shows the board with numbered positions for reference"""
        for i in range(3):
            print(f"{i * 3 + 1} | {i * 3 + 2} | {i * 3 + 3}")
            if i < 2:  # print separator line after rows 0 and 1 only
                print("--+---+--")

    def check_for_winner(self):
        winning_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]

        for line in winning_patterns:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return self.board[line[0]]
        return None  # if no one wins

    def full_board(self):
        """Checks if no empty spaces remain"""
        return " " not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == "X" else 'X'

    def play_game(self):
        print("Welcome to text-based Tic Tac Toe")
        print("Enter a number (1-9) to place your mark")
        self.print_board_numbers()
        print("\n Let's Begin\n")

        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")

            if self.current_player == 'O':  # AI's turn
                empty_positions = [i for i, spot in enumerate(self.board) if spot == " "]
                position = random.choice(empty_positions)
                print(f'AI chooses position{position + 1}')
                self.board[position] = self.current_player  # <---- Record the move
            else:  # Players turn
                try:
                    position = int(input("Choose position (1-9)")) - 1
                    if position < 0 or position > 8:
                        print('Please enter a number between (1-9)')
                        continue
                    if self.board[position] != " ":  # check for empty position
                        print("That position is already taken")
                        continue
                except ValueError:
                    print("Invalid input, please Enter a number")
                    continue

                self.board[position] = self.current_player
                #  check for winner
                winner = self.check_for_winner()
                if winner:
                    self.print_board()
                    print(f"Player {winner} Wins!!🏆")
                    break
                if self.full_board():
                    self.print_board()
                    print("It's a Tie!! 🎀")

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
