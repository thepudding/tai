from tictactoe import *
import random as rand

def random(board,player):
    ''' Basic, plays randomly. '''
    indices = list(range(9))
    rand.shuffle(indices)
    for i in indices:
        if not board[i]:
            return i

def basic_order(board,player):
    ''' Plays from top right to bottom left. '''
    for i in range(9):
        if not board[i]:
            return i

def optimized_order(board,player):
    ''' Plays center, corner, sides from lowest to highest index. '''
    for i in [4,0,2,6,8,1,3,5,7]:
        if not board[i]:
            return i

def optimized_random(board,player):
    ''' Plays center, random corner, random sides'''
    c = [0,2,6,8]
    rand.shuffle(c)
    s = [1,3,5,7]
    rand.shuffle(s)
    for i in [4]+c+s:
        if not board[i]:
            return i

def master(board,player):
    ''' Some basic optimizations. Will win and block winning. '''
    w = __winning_move(board,player)
    if w:
        return w
    b = __blocking_move(board,player)
    if b:
        return b
    for i in [4,0,2,6,8,1,3,5,7]:
        if not board[i]:
            return i

def __winning_move(board,player):
    ''' Returns the index of a move that will form 3 in a row or False if it does not exist. '''
    for i in range(9):
        if not board[i]:
            b = board[:]
            b[i] = player
            if has_won_with(b,i):
                return i
    return False

def __blocking_move(board,player):
    return __winning_move(board,'x' if player == 'o' else 'o')
