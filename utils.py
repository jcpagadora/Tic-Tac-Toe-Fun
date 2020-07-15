# Provide utility functions for running the game
from game import *

# Asks for multiplayer of computer gameplay.
def input_multiplayer_or_computer():
    while True:
        print("Type in '1' to play with a friend. Type in '2' to play with the computer.")
        x = input()
        if x == '1':
            return 1
        if x == '2':
            return 2
        else:
            print("Please follow directions!")


# Ask for player symbol
def input_symbol(player=1):
    while True:
        print("Player", player, end=", ")
        print("please type in your symbol:")
        symbol = input()
        if len(symbol) > 1:
            print("Your symbol must be one character!")
        else:
            return symbol

# Returns the game, player1, and player2
def start_game(sym1, sym2):
    board = Board()
    player1, player2 = Player(board, sym1), Player(board, sym2)
    return Game(board, player1, player2), player1, player2

def input_place(dim, symbol):
    while True:
        print("Player", symbol, end="'s turn")
        print(":")
        x_raw = input()
        x = x_raw.split(",")
        if len(x_raw) != 3 or x_raw[1] != ',' or len(x) != 2:
            print("Invalid input! Must be <row num>,<col_num>. 0,0 is top-left corner, and 2,2 is bottom-right corner.")
        else:
            try:
                i, j = int(x[0]), int(x[1])
            except ValueError:
                print("Invalid input: Entries must be integers between 0 and 2.")
                continue
            if i >= dim or j >= dim:
                print("Invalid input: out of bounds!")
            else:
                return i, j

def input_play_again():
    while True:
        print("Would you like to play again? [y/n]")
        x = input()
        if x not in ['y', 'n']:
            print("Please follow directions! Type 'y' or 'n'.")
        else:
            return x
