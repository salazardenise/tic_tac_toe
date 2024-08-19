"""
This is a Command Line Interface game of Rock Paper Scissors
for a human user versus a computer.
"""
import pyinputplus as pyip
from cli.classes.user import User
from cli.classes.user import Computer
from cli.classes.grid import Grid
from cli.constants.constants import INPUT_LIMIT, INPUT_TIMEOUT


class GameDriver:

    WELCOME_MESSAGE = "Welcome to Tic, Tac, Toe!"
    PROMPT_PLAY = "Ready to Play? (Y/N)\n"
    PROMPT_PLAY_AGAIN = "Want to play again? (Y/N)\n"

    TIE_MESSAGE = "It's a Tie!"
    USER_WON_GAME_MESSAGE_FORMAT = "Wahoo! User {} won!"
    CONGRATS_MESSAGE = "Congrats y'all!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    USER_TALLY_MESSAGE_FORMAT = "User {} won {} out of {} game(s)!"

    """
    GameDriver represents a game driver for tic, tac, toe.

    Attributes:
    -----------
    user_1 : User
    user_2: User
    grid : String[][] of ["X", "O", " "]
    """

    def __init__(self, user_1, user_2):
        self.user_1 = user_1
        self.user_2 = user_2
        self.grid = Grid()

    def _is_ready(self, message):
        is_ready = pyip.inputMenu(['Y', 'N'], 
                    prompt=message,
                    limit=INPUT_LIMIT,
                    timeout=INPUT_TIMEOUT)
        return is_ready == "Y"

    def play(self):
        print(self.WELCOME_MESSAGE)
        total_games = 0
        is_ready_prompt = self.PROMPT_PLAY

        while self._is_ready(is_ready_prompt):
            # prepare for game
            user_one_turn = True
            curr_user_won = False
            game_over = self.TIE_MESSAGE
            self.grid.reset()
            total_games += 1

            while not curr_user_won and self.grid.is_open():
                # show grid
                self.grid.pretty_print()
                # choose user
                curr_user = self.user_1
                other_user = self.user_2
                if not user_one_turn:
                    curr_user = self.user_2
                    other_user = self.user_1
                # play user
                curr_user.play_user(self.grid.grid)
                # check if user won
                if self.grid.did_user_win(curr_user.symbol):
                    curr_user_won = True
                    break
                # swtich user
                user_one_turn = not user_one_turn
            
            if curr_user_won:
                game_over = self.USER_WON_GAME_MESSAGE_FORMAT.format(
                        curr_user.name)
                curr_user.increase_num_wins()
                other_user.increase_num_loss()
            else:
                curr_user.increase_num_tie()
                other_user.increase_num_tie()

            print(game_over)
            self.grid.pretty_print()

            # ask if want to play game again
            is_ready_prompt = self.PROMPT_PLAY_AGAIN

        print(self.CONGRATS_MESSAGE)
        self.user_1.print_user_tally()
        self.user_2.print_user_tally()
