import random
import time
import os

# Dimensions of the grid
N = 30

# Function to initialize the grid
def init_grid():
    return [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]

# Function to display the grid
def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    for line in grid:
        # Use "#" for alive cells and "-" for dead cells to make it visually appealing
        print("".join("#" if cell else "-" for cell in line))
    print("\n")

# Function to count how many neighbors are alive
def count_neighbor(grid, i, j):
    nei = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < N and 0 <= y < N and (x != i or y != j):
                nei += grid[x][y]
    return nei

# Function to compute the next generation of the grid
def new_gen(grid):
    new_grid = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            nei = count_neighbor(grid, i, j)  # Fixed the variable name
            if grid[i][j] == 1:
                # Cell survives if it has 2 or 3 neighbors
                new_grid[i][j] = 1 if nei in [2, 3] else 0
            else:
                # Dead cell becomes alive if it has exactly 3 neighbors
                new_grid[i][j] = 1 if nei == 3 else 0
    return new_grid

# Function to run the simulation
def game_of_life():
    grid = init_grid()
    while True:
        display_grid(grid)
        grid = new_gen(grid)
        time.sleep(0.5)  # Pause for half a second between generations

# Start the simulation
game_of_life()
