import tkinter as tk
import cores as c


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
    
        self.main_grid = tk.Frame(
            self, bg=c.cor_grade, bd=3, width = 600, height = 600
        )
        self.main_grid.grid(pady=(110, 0))

## programando e defininfo a grade dos quadrados

    def make_GUI(self):
        self.cells =  []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                     bg=c.cor_quadradovazio,
                     width = 150,
                     height = 150
                )
                cell_frame.grid(row = i, column = j, padx = 5, pady = 5)
                cell_number = tk.Label(self.main_grid, bg = c.cor_quadradovazio)
                cell_number.grid(row = i, column = j)
                cell_data = {"frame": cell_frame, "number": cell_number}
            self.cells.append(row)

## aqui sera feito o placar do jogo