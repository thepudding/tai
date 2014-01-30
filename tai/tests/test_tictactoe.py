from tictactoe import *
import nose

def test_has_won():
    boards = [
              ([False]*9,                       False),
              
              ([False,'o','x',
                'o',False,'x',
                'o','x',False],                 False),
                
              (['x','o','o',
                'o','x','x',
                'o','x','x'],                     'x'),
                
              (['x','o','o',
                'o','o','x',
                'o','x','x'],                     'o'),
                
              (['o','o','x',
                'x','x','o',
                'o','x','o'],                   False),
                
              ([False,False,False,
                'x','x','x',
                'o',False,'o'],                   'x'),
              
              (['o','o','o',
                'x','o','x',
                'o','x','o'],                     'o'),
              
              (['x',False,'o',
                False,'x',False,
                'o',False,'x'],                   'x'),
              
              (['x','o','x',
                'x','o','x',
                'o','x','o'],                   False)
    ]
    
    for board, expected in boards:
        print board
        print expected
        yield check_board, board, expected

def check_board(board, expected):
    print 'Test of game: '
    pretty_print(board)
    print 'should have produced: ', expected
    assert has_won(board) == expected
    