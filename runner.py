import random
import sys
import tictactoe as t

# pretty print a board
def pp(b):
	b = [' ' if not x else x for x in b]
	print(b[0],'|',b[1],'|',b[2])
	print('- * - * -')
	print(b[3],'|',b[4],'|',b[5])
	print('- * - * -')
	print(b[6],'|',b[7],'|',b[8])
	print('')
# chain equal
def tql(lst,i,j,k):
	return lst[i] == lst[j] == lst[k]

# Returns x or o if that player has won, otherwise False
def has_won(b):
	if b[0] != False and (tql(b,0,1,2) or tql(b,0,3,6) or tql(b,0,4,8)):
		return b[0]
	elif b[4] != False and (tql(b,1,4,7) or tql(b,3,4,5) or tql(b,6,4,2)):
		return b[4]
	elif b[8] != False and (tql(b,6,7,8) or tql(b,2,5,8)):
		return b[8]
	else:
		return False

# Runs n*2 games n games p_one = 'x', p_two = 'o', then switches
def run_games(p_one, p_two, n):
	p1 = {'x':0,'o':0,False:0}
	p2 = {'x':0,'o':0,False:0}
	for i in range(n):
		r = run_game(p_one, p_two)
		p1[r] += 1
	for i in range(n):
		r = run_game(p_two, p_one)
		p2[r] += 1
	return p1,p2

def run_game(p_one, p_two, v=False):
	p = [p_one,p_two]
	xoro = ['o','x']
	b = [False]*9
	hw = False
	for i in range(9):
		ply = p[i%2](b[:],xoro[i%2])
		if b[ply]:
			if v:
				print("hey! no cheating!")
			return xoro[(i+1)%2]
		b[ply] = xoro[i%2]
		if v:
			pp(b)
		hw = has_won(b)
		if hw:
			return hw
	return False

def print_game_results(r):
	score = 2*(r[0]['o']+r[1]['x']) + r[0][False]+r[1][False]
	possible = 2*(r[0]['o']+r[1]['x']+r[0][False]+r[1][False]+r[0]['x']+r[1]['o'])
	print("As player one you: won ",r[0]['o'],", lost ",r[0]['x'],", and tied ",r[0][False])
	print("As player two you: won ",r[1]['x'],", lost ",r[1]['o'],", and tied ",r[1][False])
	print("In total you:      won ",r[0]['o']+r[1]['x'],", lost ",r[0]['x']+r[1]['o'],", and tied ",r[0][False]+r[1][False])
	print("Your score was:    ", score/possible)

# Players
def rand(board,xoro): # LEVEL 0
	indices = list(range(9))
	random.shuffle(indices)
	for i in indices:
		if not board[i]:
			return i
def ordr(board,xoro): # LEVEL 1
	for i in range(9):
		if not board[i]:
			return i
def ostr(board,xoro): # LEVEL 2
	for i in [4,0,2,6,8,1,3,5,7]:
		if not board[i]:
			return i
def ostrr(board,xoro): # LEVEL 3
	c = [0,2,6,8]
	random.shuffle(c)
	s = [1,3,5,7]
	random.shuffle(s)
	for i in [4]+c+s:
		if not board[i]:
			return i
def master(board, xoro): # LEVEL 4
	if not board[4]:
		return 4
	else:
		w = winning_move(board,xoro)
		if w:
			return w
		b = blocking_move(board,xoro)
		if b:
			return b
		for i in [0,2,6,8,1,3,5,7]:
			if not board[i]:
				return i

def winning_move(board,xoro):
	for i in range(9):
		if not board[i]:
			b = board[:]
			b[i] = xoro
			if has_won(b):
				return i
	return False

def blocking_move(board,xoro):
	return winning_move(board,'x' if xoro == 'o' else 'o')

if len(sys.argv) == 1:
	print("****** LEVEL 0 ******")
	print_game_results(run_games(t.play_next,rand,1000))
	print("****** LEVEL 1 ******")
	print_game_results(run_games(t.play_next,ordr,1000))
	print("****** LEVEL 2 ******")
	print_game_results(run_games(t.play_next,ostr,1000))
	print("****** LEVEL 3 ******")
	print_game_results(run_games(t.play_next,ostrr,1000))
	print("****** LEVEL 4 ******")
	print_game_results(run_games(t.play_next,master,1000))
else:
	r = sys.argv[1:]
	lvl = [rand,ordr,ostr,ostrr,master]
	for i in r:
		print("*"*10)
		print("Playing LEVEL "+i+" as Player 1[o]:")
		rslt = run_game(t.play_next,lvl[int(i)],True)
		if rslt == 'o':
			print('You Win ^_^')
		elif rslt == 'x':
			print('you Lose T_T')
		else:
			print("it's a draw -_-")
		print("*"*10)
		print("Playing LEVEL "+i+" as Player 2[x]:")
		rslt = run_game(lvl[int(i)],t.play_next,True)
		if rslt == 'x':
			print('You Win ^_^')
		elif rslt == 'o':
			print('you Lose T_T')
		else:
			print("it's a draw -_-")
		print("*"*10)

