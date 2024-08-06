"""
This is a Command Line Interface game of Rock Paper Scissors
for a human user versus a computer.
"""
import random
import pyinputplus as pyip


class User:
    """
    A class to represent a user, person or computer.

    Attributes:
    -----------
    name : str
        the username of the user
    symbol : str
        the symbol for the user in the game, typically X or O
    """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Computer(User):
    """
    A subclass of User which represents a Computer.

    Attributes:
    -----------
    level : int
        level of computer user
        1 corresponds to computer choosing x, y coordinates randomly
    """

    def __init__(self, level):
        User.__init__(self, "Computer", "O")
        self.level = 1

class Game:
    """
    Game represents a tic, tac, toe board

    Attributes:
    -----------
    user_1 : User
    user_2: User
    grid : String[][]
    """

    NUM_ROWS = 3
    NUM_COLS = 3

    def show_grid(self):
        print("Here is the current grid.")
        for row in self.grid:
            print(row)
        print()


    def __init__(self, user_1, computer_level=1):
        self.user_1 = User(user_1, "X")
        self.user_2 = Computer(computer_level)
        self.grid = [[" " for _ in range(self.NUM_COLS)] for _ in range(self.NUM_ROWS)]


    def play(self):
        print("Welcome to Tic, Tac, Toe!")
        user_one_turn = True
        game_over = "It's a Tie!"

        while self._grid_is_open():
            # show grid
            self.show_grid()
            # choose user
            curr_user = self.user_1
            if not user_one_turn:
                curr_user = self.user_2
            # play user
            self._play_user(curr_user)
            # check if user won
            if self._did_user_win(curr_user):
                game_over = "Wahoo! User {} won!".format(curr_user.name)
                break
            # swtich user
            user_one_turn = not user_one_turn

        print(game_over)
        self.show_grid()


    def _play_user(self, user):
        print("Current user is {}!".format(user.name))
        x, y = -1, -1

        if isinstance(user, Computer):
            while not self._is_valid_entry(x, y):
                x = random.randint(0, 2)
                y = random.randint(0, 2)
        else:  # type is a User, but not a Computer
            while not self._is_valid_entry(x, y):
                x = pyip.inputInt(prompt="Enter valid x coordinate (0, 1, 2): ",
                                 default=0, min=0, max=2, timeout=180)
                y = pyip.inputInt(prompt="Enter valid y coordinate (0, 1, 2): ",
                                 default=0, min=0, max=2, timeout=180)
        print("You have chosen ({}, {}).".format(x, y))
        self.grid[x][y] = user.symbol


    def _is_valid_entry(self, x, y):
        return 0 <= x <= 2 and 0 <= y <= 2 and self.grid[x][y] == " "


    def _did_user_win(self, user):
        # check rows
        for row in self.grid:
            count = 0
            for element in row:
                if element == user.symbol:
                    count += 1
            if count == 3:
                return True
        # check columns
        for j in range(0, 3):
            count = 0
            for i in range(0, 3):
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


    def _grid_is_open(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[i][j] == " ":
                    return True
        return False


def set_up():
    # username = pyip.inputStr(prompt="Enter username: ",
    #                          default="user x", blank=False, limit=3)
    # computer_level = pyip.inputInt(prompt="Enter computer level (1, 2): ",
    #                          default=1, min=1, max=2, limit=3)

    username = "Denise"
    computer_level = 1
    game = Game(username, computer_level)
    game.play()


if __name__ == "__main__":
    set_up()
