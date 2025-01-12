class GameBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
    def place_mark(self, row, col, mark):
        if self.board[row][col] == ' ':
            self.board[row][col] = mark
            return True
        return False
    def check_win(self, mark):
        # Check rows, columns, and diagonals for a winning combination of five marks
        for row in range(15):
            for col in range(15):
                if self.board[row][col] == mark:
                    if (self._check_line(self.board, row, col, 'row') or
                        self._check_line(self.board, col, row, 'col') or
                        self._check_line(self.board, row - 4, col - 4, 'diag1') or
                        self._check_line(self.board, row + 4, col - 4, 'diag2')):
                        return True
        return False
    def _check_line(self, board, start_row, start_col, line_type):
        if line_type == 'row':
            for col in range(5):
                if board[start_row + col][start_col] != board[start_row][start_col]:
                    return False
            return True
        elif line_type == 'col':
            for row in range(5):
                if board[row][start_col + row] != board[start_row][start_col]:
                    return False
            return True
        elif line_type == 'diag1':
            for i in range(5):
                if board[start_row - i][start_col + i] != board[start_row][start_col]:
                    return False
            return True
        elif line_type == 'diag2':
            for i in range(5):
                if board[start_row + i][start_col - i] != board[start_row][start_col]:
                    return False
            return True
    def reset_board(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]