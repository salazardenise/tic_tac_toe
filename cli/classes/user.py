import random
import pyinputplus as pyip
from cli.classes.utils import is_valid_entry
import cli.constants.constants as c

CURRENT_USER_PROMPT = "Current user is {}!"
COORDINATES_CHOSEN_PROMPT = "You have chosen ({}, {})."
USER_TALLY_MESSAGE_FORMAT = "User {} won {} out of {} game(s)!"

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
        self.num_wins = 0
        self.num_loss = 0
        self.num_tie = 0

    def play_user(self, grid):
        print(CURRENT_USER_PROMPT.format(self.name))
        x, y = -1, -1
        while not is_valid_entry(grid, x, y):
            x = pyip.inputInt(prompt=self.ENTER_X_PROMPT,
                             default=0, timeout=c.INPUT_TIMEOUT,
                             min=c.MIN_COORDINATE, 
                             max=c.MAX_COORDINATE)
            y = pyip.inputInt(prompt=self.ENTER_Y_PROMPT,
                             default=0, timeout=c.INPUT_TIMEOUT,
                             min=c.MIN_COORDINATE, 
                             max=c.MAX_COORDINATE)        
            print(COORDINATES_CHOSEN_PROMPT.format(x, y))
        grid[x][y] = self.symbol

    def increase_num_wins(self):
        self.num_wins += 1

    def increase_num_loss(self):
        self.num_loss += 1

    def increase_num_tie(self):
        self.num_tie += 1

    def print_user_tally(self):
        print(USER_TALLY_MESSAGE_FORMAT.format(
            self.name, 
            self.num_wins, 
            self.num_wins + self.num_loss + self.num_tie,
            ))


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
    COMPUTER_SYMBOL = c.SYMBOL_O
    LEVELS = [1, 2, 3, 4]
    UNKNOWN_LEVEL_FORMAT = "unknown level {}"

    def __init__(self, level):
        if level not in self.LEVELS:
            raise Exception(self.UNKNOWN_LEVEL_FORMAT.format(level))
        User.__init__(self, self.COMPUTER_NAME, self.COMPUTER_SYMBOL)
        self.level = level

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
            x, y = self._play_to_block(grid)
        # Level 4: choose spot to win first
        elif self.level == 4:
            x, y = self._play_to_win(grid)
        else:
            raise Exception(self.UNKNOWN_LEVEL_FORMAT.format(self.level))

        print(COORDINATES_CHOSEN_PROMPT.format(x, y))
        grid[x][y] = self.symbol

    def _play_first_open_spot(self, grid):
        x, y = -1, -1
        for i in range(0, c.NUM_ROWS):
            for j in range(0, c.NUM_COLS):
                if grid[i][j] == c.SYMBOL_BLANK:
                    return (i, j)
        return (x, y)

    def _play_random_spot(self, grid):
        x, y = -1, -1
        while not is_valid_entry(grid, x, y):
            x = random.randint(c.MIN_COORDINATE, c.MAX_COORDINATE)
            y = random.randint(c.MIN_COORDINATE, c.MAX_COORDINATE)
        return (x, y)

    # TODO: readability for both play to block and play to win methods
    def _play_to_block(self, grid):
        # check rows
        for i in range(0, c.NUM_ROWS):
            coordinates_possible = []
            count = 0
            for j in range(0, c.NUM_COLS):
                if grid[i][j] == c.SYMBOL_X:
                    count += 1
                elif grid[i][j] == c.SYMBOL_BLANK:
                    coordinates_possible.append((i, j))
            if count == 2 and len(coordinates_possible) > 0:
                return coordinates_possible[0]
        # check columns
        for j in range(0, c.NUM_COLS):
            coordinates_possible = []
            count = 0
            for i in range(0, c.NUM_ROWS):
                if grid[i][j] == c.SYMBOL_X:
                    count += 1
                elif grid[i][j] == c.SYMBOL_BLANK:
                    coordinates_possible.append((i, j))
            if count == 2 and len(coordinates_possible) > 0:
                return coordinates_possible[0]
        # check diagonal top left to bottom right
        coordinates_possible = []
        count = 0
        for i, j in [(0, 0), (1, 1), (2, 2)]:
            if grid[i][j] == c.SYMBOL_X:
                count += 1
            elif grid[i][j] == c.SYMBOL_BLANK:
                coordinates_possible.append((i, j))
        if count == 2 and len(coordinates_possible) > 0:
            return coordinates_possible[0]
        # check diagonal top right right to bottom left
        coordinates_possible = []
        count = 0
        for i, j in [(2, 0), (1, 1), (0, 2)]:
            if grid[i][j] == c.SYMBOL_X:
                count += 1
            elif grid[i][j] == c.SYMBOL_BLANK:
                coordinates_possible.append((i, j))
        if count == 2 and len(coordinates_possible) > 0:
            return coordinates_possible[0]
        # if other user is not about to win, pick first open spot
        return self._play_first_open_spot(grid)

    def _play_to_win(self, grid):
        # check rows
        for i in range(0, c.NUM_ROWS):
            count = 0
            coordinate_possible = None
            for j in range(0, c.NUM_COLS):
                if grid[i][j] == self.symbol:
                    count += 1
                elif grid[i][j] == c.SYMBOL_BLANK:
                    coordinate_possible = (i, j)
            if count == 2 and coordinate_possible:
                return coordinate_possible
        # check columns
        for j in range(0, c.NUM_COLS):
            coordinate_possible = None
            count = 0
            for i in range(0, c.NUM_ROWS):
                if grid[i][j] == self.symbol:
                    count += 1
                elif grid[i][j] == c.SYMBOL_BLANK:
                    coordinate_possible = (i, j)
            if count == 2 and coordinate_possible:
                return coordinate_possible
        # check diagonal top left to bottom right
        coordinate_possible = None
        count = 0
        for i, j in [(0, 0), (1, 1), (2, 2)]:
            if grid[i][j] == self.symbol:
                count += 1
            elif grid[i][j] == c.SYMBOL_BLANK:
                coordinate_possible = (i, j)
        if count == 2 and coordinate_possible:
            return coordinate_possible
        # check diagonal top right right to bottom left
        coordinate_possible = None
        count = 0
        for i, j in [(2, 0), (1, 1), (0, 2)]:
            if grid[i][j] == self.symbol:
                count += 1
            elif grid[i][j] == c.SYMBOL_BLANK:
                coordinate_possible = (i, j)
        if count == 2 and coordinate_possible:
            return coordinate_possible
        # if can't win, try to block other user from winning
        return self._play_to_block(grid)