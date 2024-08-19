from unittest import TestCase, mock
import cli.classes.game_driver as gd
import cli.classes.user as u
import cli.constants.constants as c

class TestCliGameDriver(TestCase):

    # called before tests in class are called
    @classmethod
    def setUpClass(cls):
        cls.user_name_1 = "test user"
        cls.computer_level_1 = 1
        
    # called before each test
    def setUp(self):
        pass

    # mock print() method
    # https://realpython.com/lessons/mocking-print-unit-tests/
    @mock.patch('builtins.print')
    def test_play_no_games(self, mock_print):
        user_1 = u.User(self.user_name_1, c.SYMBOL_X)
        user_2 = u.Computer(self.computer_level_1)
        driver = gd.GameDriver(user_1, user_2)
        # mock driver's _is_ready() method
        # https://docs.python.org/3/library/unittest.mock-examples.html#mock-patching-methods
        driver._is_ready = mock.MagicMock(name="_is_ready", return_value=False)
        driver.play()
        # no game is played at all
        u1 = driver.user_1
        u2 = driver.user_2
        mock_print.assert_has_calls([
            mock.call(driver.WELCOME_MESSAGE),
            mock.call(driver.CONGRATS_MESSAGE),
            mock.call(u.USER_TALLY_MESSAGE_FORMAT.format(u1.name, 0, 0)),
            mock.call(u.USER_TALLY_MESSAGE_FORMAT.format(u2.name, 0, 0)),
            ])
        self.assertEqual(0, driver.user_1.num_wins)
        self.assertEqual(0, driver.user_1.num_loss)
        self.assertEqual(0, driver.user_2.num_wins)
        self.assertEqual(0, driver.user_2.num_loss)

    @mock.patch('builtins.print')
    def test_play_1_game_and_user_1_wins(self, mock_print):
        user_1 = u.User(self.user_name_1, c.SYMBOL_X)
        # computer level 1 will just choose first available spot
        user_2 = u.Computer(self.computer_level_1)
        # we will mock user_1's choices
        turn = 1
        def mock_user_1_play(grid):
            nonlocal turn
            match turn:
                case 1:
                    grid[0][0] = user_1.symbol
                    # and then computer will choose 0, 1
                case 2:
                    grid[0][2] = user_1.symbol
                    # and then computer will choose 1, 0
                case 3: 
                    grid[1][1] = user_1.symbol
                    # and then computer will choose 1, 2
                case 4:
                    grid[2][0] = user_1.symbol
                    # and then this user wins
                case _:  # the fall back case
                    raise Exception("test setup incorrect")
            turn += 1
        user_1.play_user = mock_user_1_play
        # let's play
        driver = gd.GameDriver(user_1, user_2)
        driver._is_ready = mock.MagicMock(name="_is_ready", side_effect=[True, False])
        driver.play()
        u1 = driver.user_1
        u2 = driver.user_2
        mock_print.assert_has_calls([
            mock.call(driver.WELCOME_MESSAGE),
            mock.call(driver.CONGRATS_MESSAGE),
            mock.call(driver.USER_WON_GAME_MESSAGE_FORMAT.format(u1.name)),
            mock.call(u.USER_TALLY_MESSAGE_FORMAT.format(u1.name, 1, 1)),
            mock.call(u.USER_TALLY_MESSAGE_FORMAT.format(u2.name, 0, 1)),
            ], any_order=True)
        self.assertEqual(1, driver.user_1.num_wins)
        self.assertEqual(0, driver.user_1.num_loss)
        self.assertEqual(0, driver.user_2.num_wins)
        self.assertEqual(1, driver.user_2.num_loss)


    @mock.patch('builtins.print')
    def test_play_1_game_and_user_1_wins_alternate(self, mock_print):
        user_1 = u.User(self.user_name_1, c.SYMBOL_X)
        # computer level 1 will just choose first available spot
        user_2 = u.Computer(self.computer_level_1)
        # we will mock user_1's choices
        turn = 1
        def mock_user_1_play(grid):
            nonlocal turn
            match turn:
                case 1:
                    grid[0][0] = user_1.symbol
                    # and then computer will choose 0, 1
                case 2:
                    grid[0][2] = user_1.symbol
                    # and then computer will choose 1, 0
                case 3: 
                    grid[1][1] = user_1.symbol
                    # and then computer will choose 1, 2
                case 4:
                    grid[2][0] = user_1.symbol
                    # and then this user wins
                case _:  # the fall back case
                    raise Exception("test setup incorrect")
            turn += 1
        user_1.play_user = mock_user_1_play
        # let's play
        driver = gd.GameDriver(user_1, user_2)
        driver._is_ready = mock.MagicMock(name="_is_ready", side_effect=[True, False])
        driver.play()
        u1 = driver.user_1
        u2 = driver.user_2
        mock_print.assert_has_calls([
            mock.call(driver.WELCOME_MESSAGE),
            mock.call(driver.CONGRATS_MESSAGE),
            mock.call(driver.USER_WON_GAME_MESSAGE_FORMAT.format(u1.name)),
            mock.call(u.USER_TALLY_MESSAGE_FORMAT.format(u1.name, 1, 1)),
            mock.call(u.USER_TALLY_MESSAGE_FORMAT.format(u2.name, 0, 1)),
            ], any_order=True)
        self.assertEqual(1, driver.user_1.num_wins)
        self.assertEqual(0, driver.user_1.num_loss)
        self.assertEqual(0, driver.user_2.num_wins)
        self.assertEqual(1, driver.user_2.num_loss)
        expected_grid = [['X', 'O', 'X'],
                         ['O', 'X', 'O'],
                         ['X', ' ', ' ']]
        self.assertEqual(expected_grid, driver.grid.grid)






