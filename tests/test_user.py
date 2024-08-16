import unittest
from cli.classes import user as u
import cli.constants.constants as c


class TestUser(unittest.TestCase):

    # called before tests in class are called
    @classmethod
    def setUpClass(cls):
        cls.name = "Test User"
        cls.user_human = u.User(cls.name, c.SYMBOL_X)

    # called before each test
    def setUp(self):
        pass

    def test_constructor(self):
        self.assertEqual(self.name, self.user_human.name)
        self.assertEqual(c.SYMBOL_X, self.user_human.symbol)

    def test_increase_num_wins(self):
        user = u.User(self.name, c.SYMBOL_X)
        self.assertEqual(0, user.num_wins)
        self.assertEqual(0, user.num_loss)
        user.increase_num_wins()
        self.assertEqual(1, user.num_wins)
        self.assertEqual(0, user.num_loss)

    def test_increase_num_losses(self):
        user = u.User(self.name, c.SYMBOL_X)
        self.assertEqual(0, user.num_wins)
        self.assertEqual(0, user.num_loss)
        user.increase_num_loss()
        self.assertEqual(0, user.num_wins)
        self.assertEqual(1, user.num_loss)
