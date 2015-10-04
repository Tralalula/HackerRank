from __future__ import print_function

grid = []
n = int(raw_input())
for _ in xrange(n):
    grid.append([int(i) for i in raw_input()])

for i in xrange(1, n - 1):
    for j in xrange(1, n - 1):
        cell = grid[i][j]
        if cell > grid[i-1][j] and cell > grid[i+1][j] and cell > grid[i][j-1] and cell > grid[i][j+1]:
            grid[i][j] = "X"

for g in grid:
    print (*g, sep='')