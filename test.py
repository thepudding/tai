import runner as r
import unittest

class TicTacToeRunnerTest(unittest.TestCase):
    def setUp(self):
        self.empty = [False]*9
        self.empty_row = [False]*3+['x']*3+['o',False,'o']
        self.o_win = ['o']*3 + ['x','o']*3
        self.x_win = ['x',False,'o',False]*2+['x']
        self.tie = ['x','o','x']*2+['o','x','o']

    # Test if the game is over
    def test_has_won(self):
        self.assertEqual(r.has_won(self.empty), False)
        self.assertEqual(r.has_won(self.empty_row), 'x')
        self.assertEqual(r.has_won(self.o_win), 'o')
        self.assertEqual(r.has_won(self.x_win), 'x')
        self.assertEqual(r.has_won(self.tie), False)

    # Test chained equals
    def test_tql(self):
        self.assertEqual(r.tql(self.tie,0,1,2), False)
        self.assertEqual(r.tql(self.empty,0,1,2), True)
        self.assertEqual(r.tql(self.x_win,0,4,8), True)