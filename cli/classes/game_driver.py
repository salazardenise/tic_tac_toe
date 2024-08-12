"""
This is a Command Line Interface game of Rock Paper Scissors
for a human user versus a computer.
"""
import pyinputplus as pyip
from cli.classes.user import User
from cli.classes.user import Computer
from cli.classes.grid import Grid
from cli.constants.constants import SYMBOL_X


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
        self.user_1 = User(user_1, SYMBOL_X)
        self.user_2 = Computer(computer_level)
        self.grid = Grid()


    def play(self):
        print("Welcome to Tic, Tac, Toe!")
        total_games = 0

        is_ready = pyip.inputMenu(['Y', 'N'], 
                    prompt="Ready to Play? (Y/N)\n")
        while is_ready == "Y":

            # prepare for game
            user_one_turn = True
            game_over = "It's a Tie!"
            self.grid.reset()
            total_games += 1

            while self.grid.is_open():
                # show grid
                self.grid.pretty_print()
                # choose user
                curr_user = self.user_1
                if not user_one_turn:
                    curr_user = self.user_2
                # play user
                curr_user.play_user(self.grid.grid)
                # check if user won
                if self.grid.did_user_win(curr_user.symbol):
                    game_over = "Wahoo! User {} won!".format(curr_user.name)
                    curr_user.increase_num_wins()
                    break
                # swtich user
                user_one_turn = not user_one_turn
            
            print(game_over)
            self.grid.pretty_print()

            # ask if want to play game
            is_ready = pyip.inputMenu(['Y', 'N'], 
                        prompt="Want to play again? (Y/N)\n")
            print("Congrats y'all!")
            print("User {} won {} out of {} game(s)!".format(
                self.user_1.name, self.user_1.num_wins, total_games))
            print("User {} won {} out of {} game(s)!".format(
                self.user_2.name, self.user_2.num_wins, total_games))
