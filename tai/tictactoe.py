'''
TIC TAC TOE
===========

Functions for a Tic Tac Toe game.

A `board` is of type list
	- for the first move (for player one), board will look like this:
	  [False, False, False, False, False, False, False, False, False]
	- here is a finished game where 'x' has won:
	  ['o', 'o', 'x', 'o', 'o', False, 'x', 'x', 'x']
	- the list indices correspond to the board like so:
		0 | 1 | 2
		- * - * -
		3 | 4 | 5
		- * - * -
		6 | 7 | 8

Each space of the board will either be 'x', 'o', or False
'''

'''
    WIN CONDITIONS
    --------------
    This set of functions checks for various win conditions.
    `has_won` checks for all possible win conditions.
'''
def has_won(board):
    ''' Returns x or o if that player has won, otherwise False '''
    for i in [4,0,8]: # Check the middle, then top left, finally bottom right
        if has_won_with(board, i):
            return board[i]
    return False # No one has won


def has_won_with(board, i):
    ''' Returns True if the move in `board[i]` is part of a 3 in a row. '''
    # Make sure someone has played at i
    # Then check for possible wins
    return i and (row_win(board, i) or col_win(board, i) or diag_win(board, i))


# Helpers for `has_won_with`
def row_win(board, i):
    ''' Returns True if the row `i` is part of forms a 3 in a row. '''
    row = i - i%3
    return board[row] == board[row+1] == board[row+2]
def col_win(board, i):
    ''' Returns True if the column `i` is part of forms a 3 in a row. '''
    col = i%3
    return board[col] == board[col+3] == board[col+6]
def diag_win(board, i):
    ''' Returns True if a diagonal `i` is part of forms a 3 in a row. '''
    return back_diag_win(board,i) or forward_diag_win(board,i)

def forward_diag_win(board,i):
    return i in [2,4,6] and board[2] == board[4] == board[6]
def back_diag_win(board,i):
    return i in [0,4,8] and board[0] == board[4] == board[8]

'''
    UTILS
    -----
'''
def pretty_print(board):
    ''' Pretty prints a tic tac toe board. '''
    # Copy board to new list replacing False with ' '
    board = [' ' if not x else x for x in board]
    # Print each line of the board
    print board[0],'|',board[1],'|',board[2]
    print '- * - * -'
    print board[3],'|',board[4],'|',board[5]
    print '- * - * -'
    print board[6],'|',board[7],'|',board[8]