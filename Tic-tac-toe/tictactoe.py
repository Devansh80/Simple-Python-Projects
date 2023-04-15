class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        
    def display_board(self):
        print("+---+---+---+")
        print("| {} | {} | {} |".format(self.board[0], self.board[1], self.board[2]))
        print("+---+---+---+")
        print("| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5]))
        print("+---+---+---+")
        print("| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8]))
        print("+---+---+---+")
        
    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"
        else:
            print("Invalid move. Please try again.")
            
    def check_winner(self):
        # check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]
        # check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return self.board[i]
        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]
        # check for tie
        if " " not in self.board:
            return "Tie"
        # no winner yet
        return None
            
def main():
    game = TicTacToe()
    while True:
        game.display_board()
        move = int(input("Player {}: Enter a position (1-9): ".format(game.current_player)))
        game.make_move(move-1)
        winner = game.check_winner()
        if winner:
            game.display_board()
            if winner == "Tie":
                print("It's a tie!")
            else:
                print("Player {} wins!".format(winner))
            break

if __name__ == '__main__':
    main()

