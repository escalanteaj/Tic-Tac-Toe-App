import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedStyle

starting_player = 'X'  # Global variable to track starting player
current_player = starting_player

def check_win():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def check_draw():
    # Check if the game is a draw
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def on_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        winner = check_win()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            if winner == 'X':
                x_wins.set(x_wins.get() + 1)
            else:
                o_wins.set(o_wins.get() + 1)
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            ties.set(ties.get() + 1)
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            turn_label.config(text=f"Turn: Player {current_player}")

def reset_game():
    global current_player, board, starting_player
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)
    starting_player = 'O' if starting_player == 'X' else 'X'  # Swap starting player
    current_player = starting_player
    turn_label.config(text=f"Turn: Player {current_player}")

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Set window size and center it
window_width = 450
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Apply Radiance style
style = ThemedStyle(root)
style.set_theme("radiance")

# Create columns to center the content horizontally
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# Game board
buttons = [[0 for _ in range(3)] for _ in range(3)]
board = [["" for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('Arial', 20), width=5, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i+1, column=j+1, padx=5, pady=5)

# Label to indicate player's turn
turn_label = tk.Label(root, text="Turn: Player X", font=('Arial', 14))
turn_label.grid(row=0, column=0, columnspan=5, pady=(20, 0))

# Scoreboard
x_wins = tk.IntVar()
o_wins = tk.IntVar()
ties = tk.IntVar()

x_wins.set(0)
o_wins.set(0)
ties.set(0)

x_label = tk.Label(root, text="Player X wins:", font=('Arial', 12))
x_label.grid(row=5, column=1, sticky="e")
x_score = tk.Label(root, textvariable=x_wins, font=('Arial', 12))
x_score.grid(row=5, column=2, sticky="w")

o_label = tk.Label(root, text="Player O wins:", font=('Arial', 12))
o_label.grid(row=6, column=1, sticky="e")
o_score = tk.Label(root, textvariable=o_wins, font=('Arial', 12))
o_score.grid(row=6, column=2, sticky="w")

tie_label = tk.Label(root, text="Ties:", font=('Arial', 12))
tie_label.grid(row=7, column=1, sticky="e")
tie_score = tk.Label(root, textvariable=ties, font=('Arial', 12))
tie_score.grid(row=7, column=2, sticky="w")

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.grid(row=8, column=0, columnspan=5, pady=(20, 10))

current_player = 'X'

root.mainloop()