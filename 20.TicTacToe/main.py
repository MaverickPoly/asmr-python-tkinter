import tkinter as tk
from tkinter import messagebox


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.geometry("400x400")
        self.resizable(False, False)

        self.current = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.build_buttons()

        for i in range(3):
            self.rowconfigure(i, weight=1)
            
        for i in range(3):
            self.columnconfigure(i, weight=1)


        self.mainloop()

    def build_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self,
                    text="",
                    font=("Arial", 25),
                    command=lambda r=row, c=col: self.make_move(r, c),
                )
                button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current
            self.buttons[row][col].configure(text=self.current)

            if self.is_winner():
                messagebox.showinfo("Game Over", f"Player {self.current} won!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It is a draw")
                self.reset_board()
            else:
                self.current = "O" if self.current == "X" else "X"

    def is_winner(self):
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

    def is_draw(self):
        return all(self.board[row][col] for col in range(3) for row in range(3))

    def reset_board(self):
        self.current = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(text="")



if __name__ == "__main__":
    TicTacToe()
