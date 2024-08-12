"""
This is a Command Line Interface game of Tic Tac Toe
for a human user versus a computer.
"""
import pyinputplus as pyip
from cli.classes.game_driver import GameDriver as CliGameDriver
import cli.constants.constants as c


def set_up_game():
    username = pyip.inputStr(prompt="Enter username: ",
                             default="user x", 
                             blank=False, 
                             limit=c.INPUT_LIMIT)
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
    game = CliGameDriver(username, computer_level)
    return game


if __name__ == "__main__":

    game = set_up_game()
    game.play()
