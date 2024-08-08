from enum import Enum
import random
import pyinputplus as pyip

CURRENT_USER_PROMPT = "Current user is {}!"
COORDINATES_CHOSEN_PROMPT = "You have chosen ({}, {})."


class UserSymbol(Enum):
    X = "X"
    O = "O"
    Blank = " "

class User:
    """
    A class to represent a user - person or computer.

    Attributes:
    -----------
    name : str
        the username of the user
    symbol : str
        the symbol for the user in the game, typically X or O
    """

    ENTER_X_PROMPT = "Enter valid x coordinate (0, 1, 2): "
    ENTER_Y_PROMPT = "Enter valid y coordinate (0, 1, 2): "

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play_user(self, grid):
        print(CURRENT_USER_PROMPT.format(self.name))
        x, y = -1, -1
        while not grid.is_valid_entry(x, y):
            x = pyip.inputInt(prompt=self.ENTER_X_PROMPT,
                             default=0, timeout=180,
                             min=grid.MIN_COORDINATE, 
                             max=grid.MAX_COORDINATE)
            y = pyip.inputInt(prompt=self.ENTER_Y_PROMPT,
                             default=0, timeout=180,
                             min=grid.MIN_COORDINATE, 
                             max=grid.MAX_COORDINATE)        
            print(COORDINATES_CHOSEN_PROMPT.format(x, y))
        grid.grid[x][y] = self.symbol


class Computer(User):
    """
    A subclass of User which represents a Computer.

    Attributes:
    -----------
    level : int
        level of computer user
        1 corresponds to computer choosing first opening found
        2 corresponds to computer choosing x, y coordinates randomly
        3 corresponds to computer blocks other users win, if found
    """

    COMPUTER_NAME = "Computer"
    COMPUTER_SYMBOL = UserSymbol.O.value
    LEVELS = [1, 2, 3]

    def __init__(self, level):
        if level not in self.LEVELS:
            raise Exception("unknown level {}".format(level))
        User.__init__(self, self.COMPUTER_NAME, self.COMPUTER_SYMBOL)
        self.level = level
        print("created computer with level {}".format(self.level))

    def play_user(self, grid):
        print(CURRENT_USER_PROMPT.format(self.name))
        x, y = -1, -1
        # Level 1: choose 1st opening found
        if self.level == 1:
            x, y = self._play_first_open_spot(grid)
        # Level 2: choose coordinates randomnly
        elif self.level == 2:
            x, y = self._play_random_spot(grid)     
        # Level 3: choose a spot that other user is about to win
        elif self.level == 3:
            x, y = self._play_smart_spot(grid)
        else:
            raise Exception("unknown level {}".format(self.level))

        print(COORDINATES_CHOSEN_PROMPT.format(x, y))
        grid.grid[x][y] = self.symbol

    def _play_first_open_spot(self, grid):
        x, y = -1, -1
        for i in range(0, grid.NUM_ROWS):
            for j in range(0, grid.NUM_COLS):
                if grid.grid[i][j] == " ":
                    x, y = i, j
                    break
        return (x, y)

    def _play_random_spot(self, grid):
        x, y = -1, -1
        while not grid.is_valid_entry(x, y):
            x = random.randint(grid.MIN_COORDINATE, grid.MAX_COORDINATE)
            y = random.randint(grid.MIN_COORDINATE, grid.MAX_COORDINATE)
        return (x, y)

    def _play_smart_spot(self, grid):
        # check rows
        for i in range(0, grid.NUM_ROWS):
            coordinates_possible = []
            count = 0
            for j in range(0, grid.NUM_COLS):
                if grid.grid[i][j] == UserSymbol.X.value:
                    count += 1
                elif grid.grid[i][j] == UserSymbol.Blank.value:
                    coordinates_possible.append((i, j))
            if count == 2 and len(coordinates_possible) > 0:
                return coordinates_possible[0]
        # check columns
        for j in range(0, grid.NUM_COLS):
            coordinates_possible = []
            count = 0
            for i in range(0, grid.NUM_ROWS):
                if grid.grid[i][j] == UserSymbol.X.value:
                    count += 1
                elif grid.grid[i][j] == UserSymbol.Blank.value:
                    coordinates_possible.append((i, j))
            if count == 2 and len(coordinates_possible) > 0:
                return coordinates_possible[0]
        # check diagonal top left to bottom right
        coordinates_possible = []
        count = 0
        for i, j in [(0, 0), (1, 1), (2, 2)]:
            if grid.grid[i][j] == UserSymbol.X.value:
                count += 1
            elif grid.grid[i][j] == UserSymbol.Blank.value:
                coordinates_possible.append((i, j))
        if count == 2 and len(coordinates_possible) > 0:
            return coordinates_possible[0]
        # check diagonal top right right to bottom left
        coordinates_possible = []
        count = 0
        for i, j in [(2, 0), (1, 1), (0, 2)]:
            if grid.grid[i][j] == UserSymbol.X.value:
                count += 1
            elif grid.grid[i][j] == UserSymbol.Blank.value:
                coordinates_possible.append((i, j))
        if count == 2 and len(coordinates_possible) > 0:
            return coordinates_possible[0]
        return self._play_first_open_spot(grid)
