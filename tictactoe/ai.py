import sys
sys.setrecursionlimit(10000)

def is_winner(board, player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def is_board_full(board):
    return ' ' not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
    if is_winner(board, 'O'):  # AI wins
        return 10 - depth
    if is_winner(board, 'X'):  # Human wins
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for move in get_available_moves(board):
            new_board = board[:]
            new_board[move] = 'O'
            eval_score = minimax(new_board, depth + 1, False, alpha, beta)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            new_board = board[:]
            new_board[move] = 'X'
            eval_score = minimax(new_board, depth + 1, True, alpha, beta)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    import random
    import random
    moves = get_available_moves(board)
    return random.choice(moves) if moves else None


