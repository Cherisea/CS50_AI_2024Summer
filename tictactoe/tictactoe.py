"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    elif terminal(board):
        return None

    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_set.add((i, j))

    return action_set


def result(board, action):
    """
    Update the board after making a move (i, j) on the board.

    Parameters:
        board: current state of the board
        action: a tuple containing the row and column of a move

    Return: a new board resulting from action
    """
    new_board = copy.deepcopy(board)

    # Check if action is a two integer tuple
    if len(action) != 2:
        raise Exception("Action must be a tuple containing two integers.")

    # Check if both integers are within bounds
    row, col = action[0], action[1]
    if not is_valid(row) or not is_valid(col):
        raise ValueError(
            "Row and column must be between 0 and 2, both inclusive.")

    # Check if target cell is already occupied
    if board[row][col] != EMPTY:
        raise Exception("Invalid move: cell already taken.")

    new_board[row][col] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Hardcoded version only applicable to this board. Need optimization for a larger board
    for i in range(3):
        # Horizontal check
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != EMPTY):
            return board[i][0]
        # Verticla check
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != EMPTY):
            return board[0][i]

    # Diagonal check
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) \
            and board[1][1] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == None:
                    return False

        return True

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None

    # X is maximizing player since a larger final result favors X
    if player(board) == X:
        max_evl = -math.inf
        max_move = None

        # Get the maximum evaluation from all mins
        for act in actions(board):
            min_score = min_value(result(board, act))
            if min_score > max_evl:
                max_evl = min_score
                max_move = act
        return max_move

    # Correspondingly, O is the minimizing player
    if player(board) == O:
        min_evl = math.inf
        min_move = None

        for act in actions(board):
            max_score = max_value(result(board, act))
            if max_score <= min_evl:
                min_evl = max_score
                min_move = act
        return min_move


def min_value(board):
    """
    Return the minimum value from all maximum outcomes.
    """
    if terminal(board):
        return utility(board)

    # Iterate through all possible actions and select the min value from them
    min_val = math.inf
    for action in actions(board):
        min_val = min(min_val, max_value(result(board, action)))

    return min_val


def max_value(board):
    """
    Return the maximum value from all minimum results.
    """
    if terminal(board):
        return utility(board)

    # Iterate through all possible actions and select the max
    max_val = -math.inf
    for action in actions(board):
        max_val = max(max_val, min_value(result(board, action)))

    return max_val


def is_same(cell1, cell2):
    """
    Check if two cells are the same.

    Parameters:
        cell1: first cell
        cell2: second cell

    Return: true if they are the same and false otherwise
    """
    if cell1 == cell2:
        return True
    else:
        return False


def is_valid(cell_num):
    """
    Check if the given cell number is valid or not.

    Parameters:
        cell_num: number of the cell in a tic tac toe board

    Return: true if it's within bounds and false otherwise
    """
    if cell_num < 3 and cell_num >= 0:
        return True
    else:
        return False
