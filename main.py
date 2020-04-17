from utils import *

def main():
    # Starts a game of tic-tac-toe.
    print("Welcome to Tic-Tac-Toe!")
    while True:
        versus = input_multiplayer_or_computer()
        if versus == 1:
            sym1 = input_symbol(1)
            sym2 = input_symbol(2)
            game, player1, player2 = start_game(sym1, sym2)
            dim = game.get_board_dim()
            print("To play, please type in the row number, then the column number separated by a comma, no spaces.\n \
                  Row number and column number start at 0 and go down and right, respectively. For example, 0,0 \n \
                  would place your symbol on the top left corner. 2,2 would place your symbol on the bottom \n \
                  right corner.")
            flag = True
            while game.is_in_progress():
                print(game)
                if flag:
                    i, j = input_place(dim, sym1)
                    result = player1.place(i, j)
                else:
                    i, j = input_place(dim, sym2)
                    result = player2.place(i, j)
                if result == 0:
                    flag = not flag
            game.game_over()
            x = input_play_again()
            if x == 'n':
                return
        else:
            print("Sorry! Feature not implemented yet!")

# ========================================================

if __name__ == "__main__":
    main()
