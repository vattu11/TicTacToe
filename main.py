from TicTacToe import TicTacToe
import random as rd


# Asks the player to choose a piece between X and O
def ask_piece():

    piece = input("Choose piece O OR X: ")
    if piece == "X":
        print("You have chosen X")
        return piece
    elif piece == "O":
        print("You have chosen O")
        return piece
    else:
        print("Invalid choice")
        return ask_piece()

# Asks the player to choose a move
def ask_move(game):

    move = input("Enter row and column separated by space: ")
    move = move.split()

    if len(move) != 2:
        print("Invalid move")
        return ask_move(game)
    
    if not move[0].isdigit() or not move[1].isdigit():
        print("Invalid move")
        return ask_move(game)
    
    move = [int(x) for x in move]
    if move[0] not in range(3) or move[1] not in range(3):
        print("Invalid move")
        return ask_move(game)
    
    if game.board[move[0]][move[1]] is not None:
        print("Invalid move")
        return ask_move(game)

    return move


def main():

    while True:
        choice = input("Press e to exit and any other key to continue: ")

        if choice == "e":
            break
        else:
            piece = ask_piece()


        # Chosen piece is X so player starts first
        if piece == "X":
            game = TicTacToe()


            while not game.check_winner() and not game.check_tie():
                game.print_board()

                # Player move
                game.set_player('X')
                move = ask_move(game)
                game.make_move(move[0], move[1])

                # Robot move
                game.set_player('O')
                while True:
                    row = rd.randint(0, 2)
                    col = rd.randint(0, 2)
                    if game.board[row][col] is None:
                        game.make_move(row, col)
                        break
                    elif game.check_winner() or game.check_tie():
                        break

        # Chosen piece is O so robot starts first
        elif piece == "O":
            game = TicTacToe()


            while not game.check_winner() and not game.check_tie():


                # Robot move
                game.set_player('X')
                while True:
                    row = rd.randint(0, 2)
                    col = rd.randint(0, 2)
                    if game.board[row][col] is None:
                        game.make_move(row, col)
                        break
                    elif game.check_winner() or game.check_tie():
                        break

                game.print_board()
                if game.check_winner() or game.check_tie():
                    break

                # Player move
                game.set_player('O')
                move = ask_move(game)
                game.make_move(move[0], move[1])

        
        print("End results")
        print("|" + "-" * 20 + "|")
        game.print_board()
        game.return_winner()
        game.reset_game()



main()