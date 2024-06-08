import tkinter as tk
from tkinter import messagebox
from multiprocessing import Process, Manager

GRID_SIZE = 8


class SOSGame:
    def __init__(self):
        self.grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.current_player = "Player 1"
        self.moves_made = 0
        self.winner = None

    def reset_game(self):
        self.grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.current_player = "Player 1"
        self.moves_made = 0
        self.winner = None

    def make_move(self, row, col, letter):
        if self.grid[row][col] == '' and not self.winner:
            self.grid[row][col] = letter
            self.moves_made += 1
            if self.check_sos_parallel(row, col, letter):
                self.winner = self.current_player
            else:
                self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
            return True
        return False

    def check_sos_parallel(self, row, col, letter):
        manager = Manager()
        result = manager.dict()
        processes = []
        num_processes = 4  # Number of parallel processes
        rows_per_process = GRID_SIZE // num_processes

        for i in range(num_processes):
            start_row = i * rows_per_process
            end_row = (i + 1) * \
                rows_per_process if i != num_processes - 1 else GRID_SIZE
            process = Process(target=parallel_check, args=(
                self.grid, start_row, end_row, result))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        return any(result.values())

    def check_direction(self, row, col, letter, dx, dy):
        if letter == 'O':
            if self.is_valid(row-dx, col-dy) and self.is_valid(row+dx, col+dy):
                return self.grid[row-dx][col-dy] == 'S' and self.grid[row+dx][col+dy] == 'S'
        elif letter == 'S':
            if self.is_valid(row+dx, col+dy) and self.is_valid(row+2*dx, col+2*dy):
                return self.grid[row+dx][col+dy] == 'O' and self.grid[row+2*dx][col+2*dy] == 'S'
        return False

    def is_valid(self, row, col):
        return 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE


def parallel_check(grid, start_row, end_row, result):
    for i in range(start_row, end_row):
        for j in range(GRID_SIZE):
            if grid[i][j] in ['S', 'O']:
                if any(check_direction(grid, i, j, grid[i][j], dx, dy) for dx, dy in
                       [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]):
                    result[(i, j)] = grid[i][j]


def check_direction(grid, row, col, letter, dx, dy):
    if letter == 'O':
        if is_valid(row-dx, col-dy, grid) and is_valid(row+dx, col+dy, grid):
            return grid[row-dx][col-dy] == 'S' and grid[row+dx][col+dy] == 'S'
    elif letter == 'S':
        if is_valid(row+dx, col+dy, grid) and is_valid(row+2*dx, col+2*dy, grid):
            return grid[row+dx][col+dy] == 'O' and grid[row+2*dx][col+2*dy] == 'S'
    return False


def is_valid(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


class SOSGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.letters = ['S', 'O']
        self.current_letter = tk.StringVar()
        self.current_letter.set(self.letters[0])
        self.create_widgets()

    def create_widgets(self):
        self.root.title("SOS Game")
        self.buttons = [[tk.Button(self.root, text='', width=5, height=2, command=lambda row=i, col=j: self.on_button_click(row, col))
                         for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.buttons[i][j].grid(row=i, column=j)

        tk.Label(self.root, text="Current Player: ").grid(
            row=GRID_SIZE, column=0, columnspan=2)
        self.player_label = tk.Label(self.root, text=self.game.current_player)
        self.player_label.grid(row=GRID_SIZE, column=2, columnspan=2)

        tk.Label(self.root, text="Select Letter: ").grid(
            row=GRID_SIZE+1, column=0, columnspan=2)
        tk.Radiobutton(self.root, text="S", variable=self.current_letter,
                       value='S').grid(row=GRID_SIZE+1, column=2)
        tk.Radiobutton(self.root, text="O", variable=self.current_letter,
                       value='O').grid(row=GRID_SIZE+1, column=3)

        self.reset_button = tk.Button(
            self.root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=GRID_SIZE+2, column=0, columnspan=GRID_SIZE)

    def on_button_click(self, row, col):
        if self.game.make_move(row, col, self.current_letter.get()):
            self.buttons[row][col].config(text=self.current_letter.get())
            self.update_ui()
            if self.game.winner:
                self.show_winner()
            elif self.game.moves_made == GRID_SIZE * GRID_SIZE:
                self.show_draw()

    def update_ui(self):
        self.player_label.config(text=self.game.current_player)

    def reset_game(self):
        self.game.reset_game()
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self.buttons[row][col].config(text='', state='normal')
        self.update_ui()

    def show_winner(self):
        messagebox.showinfo("Game Over", f"{self.game.winner} wins!")
        self.disable_buttons()

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.disable_buttons()

    def disable_buttons(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self.buttons[row][col].config(state='disabled')


if __name__ == "__main__":
    game = SOSGame()
    root = tk.Tk()
    gui = SOSGUI(root, game)
    root.mainloop()
