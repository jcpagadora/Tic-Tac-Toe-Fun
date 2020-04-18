from utils import *

def main():
    # Starts a game of tic-tac-toe.
    print("Welcome to Tic-Tac-Toe!")
    while True:
        versus = input_multiplayer_or_computer()
        if versus == 1:
            sym1 = input_symbol(1)
            while True:
                sym2 = input_symbol(2)
                if sym1 == sym2:
                    print("Symbol already taken! Please type another symbol for your player.")
                else:
                    break
            game, player1, player2 = start_game(sym1, sym2)
            dim = game.get_board_dim()
            display_str = "To play, please type in the row number, then the column number separated by a comma, no spaces. "
            display_str += "Row number and column number start at 0 and go down and right, respectively."
            print(display_str)
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
        elif versus == 2:
            print("Sorry! Feature not implemented yet!")
        else:
            print("Please follow directions! 1 or 2.")

# ========================================================

if __name__ == "__main__":
    main()
