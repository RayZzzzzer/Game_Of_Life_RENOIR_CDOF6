import random
import time
import os
#dimension of the grid
N = 30

# Function that initialize the grid
def init_grid():
    return [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]

# Function to display the grid
def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    for line in grid:
        print(" ".join(str(cell) for cell in line))
    print("\n")

# Function to check how many neighbor are alive
def count_neighbor(grid, i, j):
    nei = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < N and 0 <= y < N and (x != i or y != j):
                nei += grid[x][y]
    return nei

# Function for the new gen of cells
def new_gen(grid):
    new_grid = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            nei = count_neighbor(grille, i, j)
            if grid[i][j] == 1:
                if nei == 2 or nei == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                if nei == 3:
                    new_grid[i][j] = 1
    return new_grid


# Start Simulation
#Game_of_Life()