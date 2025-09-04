class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def print_board(self):
        for i in range(3):
            print(f"{self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]}")
            if i < 2:
                print("--+---+--")

    def print_board_numbers(self):
        for i in range(3):
            print(f"{i*3+1} | {i*3+2} | {i*3+3}")
            if i < 2:
                print("--+---+--")

    def check_for_winner(self):
        patterns = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for line in patterns:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return self.board[line[0]]
        return None

    def full_board(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    # Minimax algorithm
    def minimax(self, is_maximizing):
        winner = self.check_for_winner()
        if winner == "O":  # AI wins
            return 1
        elif winner == "X":  # Player wins
            return -1
        elif self.full_board():
            return 0  # tie

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "O"
                    score = self.minimax(False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "X"
                    score = self.minimax(True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def ai_choose_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def play_game(self):
        print("Welcome to Tic Tac Toe! You are X. AI is O.")
        self.print_board_numbers()
        print("\nLet's Begin\n")

        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")

            if self.current_player == "O":
                position = self.ai_choose_move()
                print(f"AI chooses position {position+1}")
            else:
                try:
                    position = int(input("Choose position (1-9)")) - 1
                    if position < 0 or position > 8:
                        print("Enter a number 1-9")
                        continue
                    if self.board[position] != " ":
                        print("Position taken")
                        continue
                except ValueError:
                    print("Invalid input")
                    continue

            self.board[position] = self.current_player

            winner = self.check_for_winner()
            if winner:
                self.print_board()
                print(f"Player {winner} Wins! 🏆")
                break
            if self.full_board():
                self.print_board()
                print("It's a Tie! 🎀")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
