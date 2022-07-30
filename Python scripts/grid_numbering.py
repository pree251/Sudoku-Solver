import numpy as np
t=0
rows, cols = (9, 9)
np.arr = [[0 for i in range(cols)] for j in range(rows)]
for i in range(9):
    for j in range(9):
        np.arr[i][j]=t+j
    t=t+9
print(np.matrix(np.arr))