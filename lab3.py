# .____          ___.     ________  
# |    |   _____ \_ |__   \_____  \ 
# |    |   \__  \ | __ \    _(__  < 
# |    |___ / __ \| \_\ \  /       \
# |_______ (____  /___  / /______  /
#         \/    \/    \/         \/ 

from tai.runner import *
from tai.ai import *

####
# Before we begin, go to the project folder and type
# $ pydoc tai.runner
#
# Now open the python file tai/runner.py
# Notice that the comments are the same as what we just saw with pydoc
# Re-read the comments. Make sure you understand what they mean.
#
# Now look at the docs for tai.ai
# $ pydoc tai.ai
#
# It lists the sample AIs you can test your code against. To use the random ai for instance, pass it to `run_game(random, human, pretty_draw)`
# 
####

####
# YOUR GOALS:
# ----------
#     * Create an awesome AI tic-tac-toe player. The best AI will never loose,
#       although you cannot avoid all ties.
#     * Modify the human player to keep the user from 'breaking' the program.
#     * Implement a graphical drawing function with turtles. To display the board outside of the CLI
####

####
# HINTS:
# -----
#    * Make sure you understand how the board indexing works. It's is explained in the documentation for tai.runner.
#    * Read the samples function until you are sure you understand them
#    * Copy the sample functions into the python visualizer we used in class
#    * use helper functions!
#    
#    For user input `human(board,player)`:
#    ------------------------------------
#    * read up on try except
#    
#    For your AI `basic_ai(board,player)`:
#    ------------------------------------
#    * would this help?
#        random.shuffle()
#    * can you do this?
#        if 'x':
####

####
# DRAW FUNCTION
####
def pretty_draw(board):
    ''' Pretty prints a tic tac toe board. '''
    # MAGIC! Copy board to new list replacing False with ' '
    # Just trust that this line works and don't worry about it ^_^
    # If you want to see what it does, print the board array above and below the following line.
    board = [' ' if not x else x for x in board]
    # Print each line of the board
    print board[0],'|',board[1],'|',board[2]
    print '- * - * -'
    print board[3],'|',board[4],'|',board[5]
    print '- * - * -'
    print board[6],'|',board[7],'|',board[8]
    print ''

####
# PLAYERS
####
def basic_ai(board,player):
    i=0
    while i < 9:
        if not board[i]:
            return i
        i = i + 1

def human(board,player):
    '''
    Allows a human to play Tic Tac Toe from the CLI
    Currently does not check that the user's input is actually an int.
    Neither does it check that the user has selected a valid move.
    '''
    # Get the user's next move
    play = raw_input("Pick an open space (you are %s): " % player)
    # Convert the move to an int and save it back into play
    play = int(play)
    return play

####
# CODE START
####
winner = run_game(basic_ai, random, pretty_draw)
print "player", winner, "won!"