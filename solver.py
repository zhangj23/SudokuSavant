import json
import sys
import random
import numpy as np
import copy
class Solver():
    def __init__(self, grid):
        self.grid = grid
        self.solutions = []
    def possible(self, x, y, n):
        if n in self.grid[x]:
            return False
        for i in range(9):
            if self.grid[i][y] == n:
                return False
        box_x = (x // 3) * 3
        box_y = (y // 3) * 3
        for i in range(box_x, box_x+3):
            for j in range(box_y, box_y+3):
                if self.grid[i][j] == n:
                    return False
        return True
    def check(self):
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    return False
                n = self.grid[x][y]
                self.grid[x][y] = 0
                if n in self.grid[x]:
                    return False
                for i in range(9):
                    if self.grid[i][y] == n:
                        return False
                box_x = (x // 3) * 3
                box_y = (y // 3) * 3
                for i in range(box_x, box_x+3):
                    for j in range(box_y, box_y+3):
                        if self.grid[i][j] == n:
                            return False
                self.grid[x][y] = n
        return True
    def solve(self):
        if self.check():
            self.solutions.append(copy.deepcopy(self.grid))
            print(np.matrix(self.grid))
            return
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    for n in range(1, 10):
                        if self.possible(i, j, n):
                            self.grid[i][j] = n
                            self.solve()
                            self.grid[i][j] = 0
                    return None

# grid = [[0, 0, 1, 0, 3, 4, 8, 0, 0],
#         [0, 9, 0, 0, 0, 8, 0, 4, 5],
#         [8, 0, 0, 0, 9, 0, 7, 0, 0],
#         [0, 0, 0, 0, 2, 0, 9, 1, 0],
#         [0, 0, 0, 9, 0, 1, 0, 0, 0],
#         [0, 2, 9, 0, 8, 0, 0, 0, 0],
#         [0, 0, 8, 0, 1, 0, 0, 0, 2],
#         [6, 1, 0, 8, 0, 0, 0, 5, 0],
#         [0, 0, 3, 7, 5, 0, 6, 0, 0]]
# model = Solver(grid)
# model.solve()