import numpy as np
import grid
from Num_possiblity_check import possible
def solve():
    for y in range(9):
        for x in range(9):
            if (np.grid[y][x]==0):
                for n in range(1,10):
                    if possible(y,x,n):
                        np.grid[y][x]=n
                        solve()
                        np.grid[y][x]=0
                return
    print(np.grid)

solve()