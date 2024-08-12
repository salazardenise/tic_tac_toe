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
        cls.computer_4 = u.Computer(4)

    # called before each test
    def setUp(cls):
        pass

    def test_computer_unknown_level(self):
        self.assertRaises(Exception, u.Computer, -1)
        self.assertRaises(Exception, u.Computer, 0)
        self.assertRaises(Exception, u.Computer, 5)

    def test_computer_level_1_empty_grid(self):
        # computer will pick the first open spot at (0, 0)
        grid_1 = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        self.computer_1.play_user(grid_1)

        grid_expected = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        grid_expected[0][0] = "O"

        self.assertEqual(grid_expected, grid_1)

    def test_computer_level_1_nonempty_grid(self):
        # computer will pick the first open spot at (0, 1)
        grid_2 = [["X", " ", " "],
                  [" ", "O", "O"],
                  ["X", " ", "X"]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[0][1] = "O"

        self.computer_1.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_3_empty_grid(self):
        # computer will try to block first (no spot for that)
        # so will then pick the first open spot
        grid_1 = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        self.computer_3.play_user(grid_1)

        grid_expected = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        grid_expected[0][0] = "O"

        self.assertEqual(grid_expected, grid_1)

    def test_computer_level_3_nonempty_grid_smart_move_in_row(self):
        # computer will block the other user at (2, 1)
        grid_2 = [[" ", " ", "X"],
                  [" ", "O", "O"],
                  ["X", " ", "X"]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[2][1] = "O"

        self.computer_3.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_3_nonempty_grid_smart_move_in_col(self):
        # computer will block the other user at (1, 0)
        grid_2 = [["X", " ", " "],
                  [" ", "O", " "],
                  ["X", " ", " "]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[1][0] = "O"

        self.computer_3.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_3_nonempty_grid_smart_move_in_diagonal_1(self):
        # computer will block the other user at (2, 2)
        grid_2 = [["X", " ", "O"],
                  [" ", "X", " "],
                  [" ", " ", " "]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[2][2] = "O"

        self.computer_3.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_3_nonempty_grid_smart_move_in_diagonal_2(self):
        # computer will block the other user at (2, 0)
        grid_2 = [[" ", "O", "X"],
                  [" ", "X", " "],
                  [" ", " ", " "]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[2][0] = "O"

        self.computer_3.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_4_empty_grid(self):
        # computer can't win, then nothing to block, 
        # so will pick first open spot
        grid_1 = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        self.computer_4.play_user(grid_1)

        grid_expected = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
        grid_expected[0][0] = "O"

        self.assertEqual(grid_expected, grid_1)

    def test_computer_level_4_nonempty_grid_attempt_smart_move_in_row(self):
        # computer checks first row, no spot possible in first row to win
        # no spot possible to win at all actually
        # then blocks the other user at (1, 2)
        grid = [["O", "O", "X"],
                [" ", "X", " "],
                [" ", " ", "X"]]
        grid_expected = copy.deepcopy(grid)
        grid_expected[1][2] = "O"

        self.computer_4.play_user(grid)
        self.assertEqual(grid_expected, grid)

    def test_computer_level_4_nonempty_grid_smart_move_in_row(self):
        # computer will choose (1, 1) to win first
        # instead of trying to block other user at (2, 0) first
        grid_2 = [["X", " ", " "],
                  ["O", " ", "O"],
                  [" ", "X", "X"]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[1][1] = "O"

        self.computer_4.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_4_nonempty_grid_smart_move_in_col(self):
        # computer will choose (0, 1) to win first
        # instead of trying to block the other user at (1, 0) first
        grid_2 = [["X", " ", " "],
                  [" ", "O", " "],
                  ["X", "O", "X"]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[0][1] = "O"

        self.computer_4.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_4_nonempty_grid_smart_move_in_diagonal_1(self):
        # computer will choose (1, 1) to win first
        # computer will NOT first try to block (no spot for that)
        # and then picking the first open spot at (0, 1)
        grid_2 = [["O", " ", "X"],
                  ["X", " ", " "],
                  ["X", " ", "O"]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[1][1] = "O"

        self.computer_4.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)

    def test_computer_level_4_nonempty_grid_smart_move_in_diagonal_2(self):
        # computer will choose (1, 1) to win first
        # computer will NOT first try to block (no spot for that)
        # and then pick the first open spot at (0, 0)
        grid_2 = [[" ", "X", "O"],
                  ["X", " ", " "],
                  ["O", " ", "X"]]
        grid_expected = copy.deepcopy(grid_2)
        grid_expected[1][1] = "O"

        self.computer_4.play_user(grid_2)
        self.assertEqual(grid_expected, grid_2)
