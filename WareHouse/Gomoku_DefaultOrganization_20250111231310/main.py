if __name__ == "__main__":
    game_board = GameBoard()
    game_ui = GameUI(game_board)
    game_ui.root.mainloop()
    game_board.reset_board()