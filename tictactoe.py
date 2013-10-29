# .____          ___.     ________  
# |    |   _____ \_ |__   \_____  \ 
# |    |   \__  \ | __ \    _(__  < 
# |    |___ / __ \| \_\ \  /       \
# |_______ (____  /___  / /______  /
#         \/    \/    \/         \/ 

####
# Before we begin, try running the code.
# 	* In Cygwin/Terminal navigate to lab3/
# 	* type:
# 		python3 runner.pyc
#   		or
# 		py runner.pyc
#	  What did it do?
#
#	* now type:
#		python3 runner.pyc 1
#			or
#		py runner.pyc 1
#	  What did /that/ do?
####

####
# Your goal:
# 	* Create an awesome AI tic tac toe function
####

####
# Your instructions are as follows:
# 	* modify tictactoe.py (but don't rename it!)
# 	* keep it in the same directory as runner.pyc
# 	* modify the function play_next (but don't rename it!)
#     runner.pyc will use your play_next function to play the built in AIs
####

####
# Hints!
#	* use helper functions!
#	* remember this?
#		lst[0:2:6]
#	* would this help?
#		random.shuffle()
# 	* can you do this?
#		if 'x':
####

####
# play_next:
# 	* takes a `board` of type list
#		- for the first move (for player one), board will look like this:
#		  [False, False, False, False, False, False, False, False, False]
#		- here is a finished game where 'x' has won:
#		  ['o', 'o', 'x', 'o', 'o', False, 'x', 'x', 'x']
#		- the list indices correspond to the board like so:
#			0 | 1 | 2
#			– * – * –
#			3 | 4 | 5
#			- * - * -
#			6 | 7 | 8
#
#	* and a string `xoro` which will either be 'x' or 'o' and indicates which you are
#
#	* returns an integer index between 0 and 8 inclusive
#		- corresponds to a free space on the board
####
def play_next(board,xoro): # -> [0-8]
	for i in range(9):
		if not board[i]:
			return i