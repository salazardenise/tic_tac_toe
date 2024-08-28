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

    def test_increase_tic_tac_toe_num_wins(self):
        user = u.User(self.name, c.SYMBOL_X)
        self.assertEqual(0, user.get_tic_tac_toe_num_wins())
        self.assertEqual(0, user.get_tic_tac_toe_num_loss())
        self.assertEqual(0, user.get_tic_tac_toe_num_tie())
        user.increase_tic_tac_toe_num_wins()
        self.assertEqual(1, user.get_tic_tac_toe_num_wins())
        self.assertEqual(0, user.get_tic_tac_toe_num_loss())
        self.assertEqual(0, user.get_tic_tac_toe_num_tie())

    def test_increase_tic_tac_toe_num_losses(self):
        user = u.User(self.name, c.SYMBOL_X)
        self.assertEqual(0, user.get_tic_tac_toe_num_wins())
        self.assertEqual(0, user.get_tic_tac_toe_num_loss())
        self.assertEqual(0, user.get_tic_tac_toe_num_tie())        
        user.increase_tic_tac_toe_num_loss()
        self.assertEqual(0, user.get_tic_tac_toe_num_wins())
        self.assertEqual(1, user.get_tic_tac_toe_num_loss())
        self.assertEqual(0, user.get_tic_tac_toe_num_tie())

    def test_increase_tic_tac_toe_num_tied(self):
        user = u.User(self.name, c.SYMBOL_X)
        self.assertEqual(0, user.get_tic_tac_toe_num_wins())
        self.assertEqual(0, user.get_tic_tac_toe_num_loss())
        self.assertEqual(0, user.get_tic_tac_toe_num_tie())
        user.increase_tic_tac_toe_num_tie()
        self.assertEqual(0, user.get_tic_tac_toe_num_wins())
        self.assertEqual(0, user.get_tic_tac_toe_num_loss())
        self.assertEqual(1, user.get_tic_tac_toe_num_tie())
    
    @unittest.mock.patch('builtins.print')
    def test_print_user_tally_tic_tac_toe(self, mock_print):
        user = u.User(self.name, c.SYMBOL_X)
        user.print_user_tally_tic_tac_toe()
        mock_print.assert_has_calls([
            unittest.mock.call(u.USER_TALLY_TTT_MESSAGE_FORMAT.format(
                self.name, 0, 0))
            ])


