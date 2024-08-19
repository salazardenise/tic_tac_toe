import unittest
from cli.classes import grid as g
import cli.constants.constants as c

class TestGrid(unittest.TestCase):

    # called before tests in class are called
    @classmethod
    def setUpClass(cls):
        cls.grid_empty = g.Grid()

    # called before each test
    def setUp(cls):
        pass

    def test_is_open(self):
        self.assertTrue(self.grid_empty.is_open())
        grid_full = g.Grid()
        grid_full.grid = [["X", "X", "O"],
                          ["O", "O", "X"],
                          ["X", "O", "X"]]
        self.assertFalse(grid_full.is_open())

    def test_did_user_win_no(self):
        self.assertFalse(self.grid_empty.did_user_win(c.SYMBOL_X))

    def test_did_user_win_in_row(self):
        grid_1 = g.Grid()
        grid_1.grid = [["O", " ", " "],
                       ["X", "X", "X"],
                       [" ", "O", " "]]
        self.assertTrue(grid_1.did_user_win(c.SYMBOL_X))

    def test_did_user_win_in_col(self):
        grid_1 = g.Grid()
        grid_1.grid = [["O", " ", "X"],
                       [" ", " ", "X"],
                       [" ", "O", "X"]]
        self.assertTrue(grid_1.did_user_win(c.SYMBOL_X))

    def test_did_user_win_in_diag_1(self):
        grid_1 = g.Grid()
        grid_1.grid = [["X", " ", " "],
                       [" ", "X", "O"],
                       [" ", "O", "X"]]
        self.assertTrue(grid_1.did_user_win(c.SYMBOL_X))

    def test_did_user_win_in_diag_2(self):
        grid_1 = g.Grid()
        grid_1.grid = [[" ", " ", "X"],
                       [" ", "X", "O"],
                       ["X", "O", " "]]
        self.assertTrue(grid_1.did_user_win(c.SYMBOL_X))
