def play_next(board,xoro): # -> [0-8]
	for i in range(9):
		if not board[i]:
			return i