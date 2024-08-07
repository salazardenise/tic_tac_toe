from user import UserSymbol


class Grid:
    """
    Grid represents the grid of a tic, tac, toe board.

    Attributes:
    -----------
    grid : String[][] of characters ["X", "O", " "]
    """

    NUM_ROWS = 3
    NUM_COLS = 3

    MIN_COORDINATE = 0
    MAX_COORDINATE = 2

    def __init__(self):
        self.grid = [[UserSymbol.Blank.value for _ in range(self.NUM_COLS)] for _ in range(self.NUM_ROWS)]

    def is_valid_entry(self, x, y):
        return self.MIN_COORDINATE <= x <= self.MAX_COORDINATE and \
               self.MIN_COORDINATE <= y <= self.MAX_COORDINATE and \
               self.grid[x][y] == UserSymbol.Blank.value
    
    def pretty_print(self):
        print("Here is the current grid.")
        for row in self.grid:
            print(row)
        print()

    def is_open(self):
        for i in range(0, self.NUM_ROWS):
            for j in range(0, self.NUM_COLS):
                if self.grid[i][j] == UserSymbol.Blank.value:
                    return True
        return False

    def did_user_win(self, user):
        # check rows
        for row in self.grid:
            count = 0
            for element in row:
                if element == user.symbol:
                    count += 1
            if count == 3:
                return True
        # check columns
        for j in range(0, self.NUM_COLS):
            count = 0
            for i in range(0, self.NUM_ROWS):
                if self.grid[i][j] == user.symbol:
                    count += 1
            if count == 3:
                return True
        # check left to right diagonal
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == user.symbol:
            return True
        # check right to left diagonal
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == user.symbol:
            return True
        return False
