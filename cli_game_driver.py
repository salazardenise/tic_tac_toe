"""
This is a Command Line Interface game of Tic Tac Toe
for a human user versus a computer.
"""
import pyinputplus as pyip
from cli.classes.game_driver import CliGameDriver, CliTicTacToe
import cli.constants.constants as c
from cli.classes.user import User, Computer


def set_up_game():
    # set up human user
    username = pyip.inputStr(prompt="Enter username: ",
                             default="user x", 
                             blank=False, 
                             limit=c.INPUT_LIMIT)
    user_1 = User(username, c.SYMBOL_X)

    # set up computer user
    computer_prompt = "Enter computer level (1, 2, 3, 4)\n" + \
                      "* Level 1: Basic\n" + \
                      "* Level 2: Random\n" + \
                      "* Level 3: Plays to block\n" + \
                      "* Level 4: Plays to win\n"
    computer_level = pyip.inputInt(prompt=computer_prompt,
                             default=1, 
                             min=1, 
                             max=4, 
                             limit=c.INPUT_LIMIT)
    user_2 = Computer(computer_level)

    # set up game driver
    game_tic_tac_toe = CliTicTacToe(user_1, user_2)
    return game_tic_tac_toe


if __name__ == "__main__":

    game_tic_tac_toe = set_up_game()
    game_tic_tac_toe.play()
