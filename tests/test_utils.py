import unittest
import copy
from cli.classes.utils import is_valid_entry

class TestUtils(unittest.TestCase):

    # called before tests in class are called
    @classmethod
    def setUpClass(cls):
        cls.grid_empty = [[" " for _ in range(0, 3)] for _ in range(0, 3)]

    # called before each test
    def setUp(cls):
        pass

    def test_is_valid_entry(self):
        self.assertFalse(is_valid_entry(self.grid_empty, -1, 0))
        self.assertFalse(is_valid_entry(self.grid_empty, 3, 0))
        self.assertFalse(is_valid_entry(self.grid_empty, 0, -1))
        self.assertFalse(is_valid_entry(self.grid_empty, 0, 3))
        self.assertTrue(is_valid_entry(self.grid_empty, 0, 0))
        grid_1 = copy.deepcopy(self.grid_empty)
        grid_1[1][1] = "X"
        self.assertFalse(is_valid_entry(grid_1, 1, 1))