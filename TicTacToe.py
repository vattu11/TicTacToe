# Class TicTacToe

class TicTacToe:
    def __init__(self):
        self.board = [[None, None, None] for _ in range(3)]
        self.player = None


    # Functions start here

    # Prints the board's current state
    def print_board(self):
        print('    0   1   2')
        print('  ' + '-' * 13)
        for i, row in enumerate(self.board):
            print(i, '|', end='')
            for cell in row:
                if cell is None:
                    print('   |', end='')
                else:
                    print(f' {cell} |', end='')
            print('\n  ' + '-' * 13)

    # Sets the player's piece which decides are you player1 or player2
    def set_player(self, player):
        self.player = player

    # Makes a move on the board, updates the board's state
    def make_move(self, row, col):
        if self.board[row][col] is not None:
            print("Invalid move")
            return
        if self.player == "X":
            self.board[row][col] = "X"
        else:
            self.board[row][col] = "O"

    # Checks if there is a winner returns Boolean
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] is not None and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if self.board[0][i] is not None and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if self.board[0][0] is not None and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] is not None and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False
    
    # Checks if there is a tie returns Boolean
    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True


    # Resets the game
    def reset_game(self):
        self.board = [[None, None, None] for _ in range(3)]
        self.player_turn = None

    # Gives winner
    def return_winner(self):
        if self.check_winner() is True:
            print(f"Winner is: {self.player}")
        elif self.check_tie() is True:
            print("It's a tie!")
        return
    
    # End of functions