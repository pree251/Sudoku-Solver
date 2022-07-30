import numpy as np
import grid
def possible(y,x,n):
    global grid
    for i in range(0,9):
        if np.grid[y][i]==n:
            return False
    for i in range(0,9):
        if np.grid[i][x]==n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if np.grid[i+y0][j+x0]==n:
                return False
    return True
