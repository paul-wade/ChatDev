import tkinter as tk
from game_board import GameBoard
class GameUI:
    def __init__(self, game_board):
        self.game_board = game_board
        self.root = tk.Tk()
        self.create_widgets()
    def create_widgets(self):
        for row in range(15):
            for col in range(15):
                button = tk.Button(
                    self.root,
                    text=' ',
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.handle_button_click(r, c)
                )
                button.grid(row=row, column=col)
    def handle_button_click(self, row, col):
        mark = 'X' if self.game_board.place_mark(row, col, mark) else 'O'
        self._update_buttons(row, col, mark)
        if self.game_board.check_win(mark):
            self.root.title(f'{mark} wins!')
    def _update_buttons(self, row, col, mark):
        for r in range(15):
            for c in range(15):
                button = self.root.grid_slaves(row=r, column=c)
                if button:
                    button[0].config(text=button[0].cget('text'), state=(tk.NORMAL if (r, c) != (row, col) else tk.DISABLED))