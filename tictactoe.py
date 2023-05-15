import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:

    def __init__(self):
        self.player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.create_board()
        self.root.mainloop()

    def create_board(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=5, font=("Helvetica", 20), command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.player)
            self.board[row][col] = self.player
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", "Player " + self.player + " wins!")
                self.root.destroy()
                return
            if self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "Tie!")
                self.root.destroy()
                return
            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

game = TicTacToeGUI()

