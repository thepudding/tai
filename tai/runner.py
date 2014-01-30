'''
Use `run_game` to start tictactoe games between two players.
Some computer players can be found in tai.ai
'''
from tictactoe import has_won_with

def run_game(p_one, p_two, draw):
    '''
    expects two 'player' functions and a draw function.
    returns either a string 'x', 'o', or False indicating the winner.
    False indicates a cats game.
    
    The player functions
    --------------------
    p_one, p_two
    (list:board, string:player) -> integer
     * takes a `board` of type list
         - for the first move (for player one), the board will look like this:
           [False, False, False, False, False, False, False, False, False]
         - here is a finished game where 'x' has won:
           ['o', 'o', 'x', 'o', 'o', False, 'x', 'x', 'x']
         - the list indices correspond to the board like so:
            0 | 1 | 2
            - * - * -
            3 | 4 | 5
            - * - * -
            6 | 7 | 8

    * a string `player` indicates which player you are, either 'x' or 'o'

    * returns an integer index for the next move
        - e.g. `6` would indicate that your AI wants to play in 
          the bottom left corner of the board.
        - the returned value must correspond to a free space on the board,
          otherwise an IndexError will be raised.
    
    The `draw` function
    -------------------
    (list:board) -> None
    
    The `draw` function takes a board list as an argument and
    can print it any way it wishes. It does not return a value.
    '''
    # players & ox are used to toggle between players in the game loop
    players = [p_one,p_two]
    ox = ['o','x']
    
    # Board values are: False, 'o', and 'x'
    board = [False]*9
    
    # The max depth is 9
    for i in range(9):
        # call correct player function,
        # passing the current game board 
        # and player's symbol as arguments
        move = players[i%2](board[:],ox[i%2])
        
        # Raise an error if the player tried to overwrite a taken space
        if board[move]:
            raise IndexError("Invalid move! Player: %s attempted to play at index: %d on board: %s"%(ox[i%2],move,board))
        # Otherwise continue
        else:
            # Update the board state
            board[move] = ox[i%2]
            # Display the new board with the given 'run' function
            draw(board)
            
            # Check for end game
            if has_won_with(board,move):
                # Return the winner and the final board state
                return ox[i%2]
    
    # If we filled the board and there was no winner it's a cats game.
    # Return false for a cats game along with the board
    return False