"""
This is a Command Line Interface game of Rock Paper Scissors
for a human user versus a computer.
"""
import pyinputplus as pyip
from user import User, Computer, UserSymbol
from grid import Grid

class GameDriver:
    """
    GameDriver represents a game driver for tic, tac, toe.

    Attributes:
    -----------
    user_1 : User
    user_2: User
    grid : String[][] of ["X", "O", " "]
    """

    def __init__(self, user_1, computer_level=1):
        self.user_1 = User(user_1, UserSymbol.X.value)
        self.user_2 = Computer(computer_level)
        self.grid = Grid()


    def play(self):
        print("Welcome to Tic, Tac, Toe!")
        user_one_turn = True
        game_over = "It's a Tie!"

        while self.grid.is_open():
            # show grid
            self.grid.pretty_print()
            # choose user
            curr_user = self.user_1
            if not user_one_turn:
                curr_user = self.user_2
            # play user
            curr_user.play_user(self.grid)
            # check if user won
            if self.grid.did_user_win(curr_user):
                game_over = "Wahoo! User {} won!".format(curr_user.name)
                break
            # swtich user
            user_one_turn = not user_one_turn

        print(game_over)
        self.grid.pretty_print()


def set_up_game():
    username = pyip.inputStr(prompt="Enter username: ",
                             default="user x", blank=False, limit=3)
    computer_level = pyip.inputInt(prompt="Enter computer level (1, 2): ",
                             default=1, min=1, max=2, limit=3)
    game = GameDriver(username, computer_level)
    return game


if __name__ == "__main__":
    game = set_up_game()
    game.play()
