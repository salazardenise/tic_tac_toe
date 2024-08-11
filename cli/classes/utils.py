

def is_valid_entry(grid, x, y):
    return 0 <= x <= 2 and \
           0 <= y <= 2 and \
           grid[x][y] == " "