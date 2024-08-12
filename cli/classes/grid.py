import cli.constants.constants as c


class Grid:
    """
    Grid represents the grid of a tic, tac, toe board.

    Attributes:
    -----------
    grid : String[][] of characters ["X", "O", " "]
    """

    def __init__(self):
        self.grid = [[c.SYMBOL_BLANK for _ in range(c.NUM_COLS)] for _ in range(c.NUM_ROWS)]
    
    def pretty_print(self):
        print("Here is the current grid.")
        for row in self.grid:
            print(row)
        print()

    def reset(self):
        self.grid = [[c.SYMBOL_BLANK for _ in range(c.NUM_COLS)] for _ in range(c.NUM_ROWS)]

    def is_open(self):
        for i in range(0, c.NUM_ROWS):
            for j in range(0, c.NUM_COLS):
                if self.grid[i][j] == c.SYMBOL_BLANK:
                    return True
        return False

    def did_user_win(self, user_symbol):
        # check rows
        for row in self.grid:
            count = 0
            for element in row:
                if element == user_symbol:
                    count += 1
            if count == 3:
                return True
        # check columns
        for j in range(0, c.NUM_COLS):
            count = 0
            for i in range(0, c.NUM_ROWS):
                if self.grid[i][j] == user_symbol:
                    count += 1
            if count == 3:
                return True
        # check left to right diagonal
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == user_symbol:
            return True
        # check right to left diagonal
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == user_symbol:
            return True
        return False

    def __eq__(self, other):
        for i in range(0, c.NUM_ROWS):
            for j in range(0, c.NUM_COLS):
                if self.grid[i][j] != other.grid[i][j]:
                    return False
        return True
