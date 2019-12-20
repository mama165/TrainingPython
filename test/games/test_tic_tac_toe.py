import unittest
from numpy import *

from sample.games.tictactoe.tic_tac_toe import TicTacToe


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe

    def test_should_find_winner(self):
        mat = array([])
        mat_c = insert(mat, [0], [['x'], ['o'], ['o']], 0)
        print(mat_c)
        output = self.tic_tac_toe.is_winner(mat)
        self.assertEqual(True, output)


if __name__ == '__main__':
    unittest.main()
