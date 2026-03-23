class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'  # Human starts

    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def is_winner(self, player):
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(self.board[a] == self.board[b] == self.board[c] == player for a,b,c in win_conditions)

    def is_board_full(self):
        return ' ' not in self.board

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def get_board_copy(self):
        return self.board[:]

