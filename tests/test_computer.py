import unittest
import copy
from cli.classes import user as u

class TestComputer(unittest.TestCase):

    # called before tests in class are called
    @classmethod
    def setUpClass(cls):
        cls.computer_1 = u.Computer(1)
        cls.computer_2 = u.Computer(2)
        cls.computer_3 = u.Computer(3)

    # called before each test
    def setUp(cls):
        pass

    def test_computer_unknown_level(self):
        self.assertRaises(Exception, u.Computer, -1)
        self.assertRaises(Exception, u.Computer, 0)
        self.assertRaises(Exception, u.Computer, 4)

    def test_computer_level_1_empty_grid(self):
        grid_1 = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        self.computer_1.play_user(grid_1)

        grid_expected = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        grid_expected[0][0] = "O"

        self.assertEqual(grid_expected, grid_1)

    def test_computer_level_1_nonempty_grid(self):
        grid_2 = [["X", " ", " "],
                  [" ", "O", "O"],
                  ["X", " ", "X"]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[0][1] = "O"

        self.computer_1.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_3_empty_grid(self):
        grid_1 = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        self.computer_3.play_user(grid_1)

        grid_expected = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        grid_expected[0][0] = "O"

        self.assertEqual(grid_expected, grid_1)

    def test_computer_level_3_nonempty_grid_smart_move_in_row(self):
        grid_2 = [["X", " ", " "],
                  [" ", "O", "O"],
                  ["X", " ", "X"]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[2][1] = "O"

        self.computer_3.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_3_nonempty_grid_smart_move_in_col(self):
        grid_2 = [["X", " ", " "],
                  [" ", "O", " "],
                  ["X", " ", " "]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[1][0] = "O"

        self.computer_3.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_3_nonempty_grid_smart_move_in_diagonal_1(self):
        grid_2 = [["X", " ", "O"],
                  [" ", "X", " "],
                  [" ", " ", " "]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[2][2] = "O"

        self.computer_3.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_3_nonempty_grid_smart_move_in_diagonal_2(self):
        grid_2 = [[" ", "O", "X"],
                  [" ", "X", " "],
                  [" ", " ", " "]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[2][0] = "O"

        self.computer_3.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

