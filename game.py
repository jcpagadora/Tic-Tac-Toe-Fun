
class Game:
    # Game object has one board and two players. Players take turns to place symbols on the board
    # until the end state is reached (see comments to Board class below).
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.draw = True

    def is_in_progress(self):
        player_stat = max(self.player1.status(), self.player2.status())
        if player_stat:
            self.draw = False
            if self.player1.status() == 1:
                self.winner = self.player1
            else:
                self.winner = self.player2
            return False
        if self.board.is_full():
            return False
        return True

    def game_over(self):
        if self.draw:
            print("This game is a draw!")
        else:
            print("Winner is", self.winner, end="! ")

    def get_board_dim(self):
        return len(self.board)

    def __str__(self):
        return self.board.__str__()

class Board:
    # Board class to implement a tic tac toe board: a 3-by-3 (default) square grid,
    # with each square in one of three states: blank, X, or O (default)
    # Recall that the game is ended if (1) its board has an entire row, column, or diagonal consisting of
    # all X's or all O's, or (2) all spaces are occupied and condition (1) is not satisfied.
    # Here, the board is implemented using a list of rows, where it is initialized with all entries being None

    def __init__(self, dim=3):
        self.board = []
        for i in range(dim):
            self.board.append([])
            for j in range(dim):
                self.board[i].append(' ')

    def place(self, i, j, symbol):
        self.board[i][j] = symbol

    def get(self, i, j):
        return self.board[i][j]

    def __len__(self):
        return len(self.board)

    def __str__(self):
        # Important method used to print the current tic-tac-toe game at every turn
        result = ""
        for i in range(len(self.board)):
            row = self.board[i]
            for j in range(len(row)):
                result += " " + row[j] + " "
                if j < len(row) - 1:
                    result += "|"
            result += "\n"
            if i < len(self.board) - 1:
                for j in range(len(row)):
                    result += "---"
                    if j < len(row) - 1:
                        result += "|"
            result += "\n"
        return result

    def is_full(self):
        for row in self.board:
            for char in row:
                if char == ' ':
                    return False
        return True


class Player:
    # Player class. Each game has exactly two players: one that can place X's and one that places O's.

    def __init__(self, board, symbol):
        assert len(str(symbol)) == 1
        self.board = board
        self.symbol = str(symbol)
        # trackers are dictionaries that keeps track of the rows, columns, diagonals
        # of all symbols placed on the board
        self.row_tracker = [0] * len(board)
        self.col_tracker = [0] * len(board)
        self.diag_tracker = [0, 0]  # Either indices are equal or add up to len(board) - 1

    # Return 0: Success
    # Return 1: Failure
    def place(self, i, j):
        if self.board.get(i, j) != ' ':
            print("That space is already taken!")
            return 1
        if i >= len(self.board) or j >= len(self.board):
            print("Invalid input!")
            return 1
        self.board.place(i, j, self.symbol)
        # Add to row tracker
        self.row_tracker[i] += 1
        # Add to column tracker
        self.col_tracker[j] += 1
        # Add to diagonal tracker, if applicable. First diagonal of equal entries in 0th index.
        # Diagonal where indices add up to len(board) - 1 in 1st index.
        if i == j:
            self.diag_tracker[0] += 1
        if i + j == len(self.board) - 1:
            self.diag_tracker[1] += 1
        return 0

    # Get the status of the player. Return 0: Lose/Draw/In progress. Return 1: Win.
    def status(self):
        if any([x == 3 for x in self.row_tracker]) or any([x == 3 for x in self.col_tracker]) or \
                any([x == 3 for x in self.diag_tracker]):
            return 1
        return 0

    def __str__(self):
        return self.symbol


# ==============================================================================

# Some tests
if __name__ == "__main__":
    board = Board()
    p = Player(board, "X")
    p1 = Player(board, "O")
    p.place(1, 1)
    p1.place(0, 0)
    p.place(0, 1)
    p1.place(1, 0)
    print(board)
    print("row:", p.row_tracker)
    print("col:", p.col_tracker)
    print("diag:", p.diag_tracker)
    p.place(2, 1)
    print(board)
    print("row:", p.row_tracker)
    print("col:", p.col_tracker)
    print("diag:", p.diag_tracker)
    print(p1.status())
